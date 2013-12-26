__appname__ = "appstats"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

import urllib2
import json

from django.views.generic import ListView, CreateView, DetailView, FormView,\
    TemplateView, DeleteView
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from braces.views import LoginRequiredMixin

from .models import StatsProjectModel, StatsMapModel, ApiFieldsModel, CxtModel
from .forms import ApiFieldsForm, StatsCreateForm


class IndexView(TemplateView):
    template_name = "index.html"


class ManageProjectsView(LoginRequiredMixin, ListView):
    """Main list of all the statistical projects"""
    model = StatsProjectModel
    template_name = "appstats/statsprojects.html"


class StatsCreateView(LoginRequiredMixin, CreateView):
    """Creates a new instance using StatsProjectModel model"""
    model = StatsProjectModel
    template_name = "addproject.html"
    form_class = StatsCreateForm

    def form_valid(self, form):
        """
        Before saving, a new map is created for the new model. Since they are
        created at the same time, each new project's ID will be the same as
        the just created map's ID.
        """
        newmap = StatsMapModel(dateget=None, cxtposition=form.instance.cxtposition)
        newmap.save()
        form.instance.map = StatsMapModel.objects.latest('id')
        return super(StatsCreateView, self).form_valid(form)


class StatsProjectView(LoginRequiredMixin, DetailView):
    """
    Returns a view with project's details, taking some context information
    from other tables.
    """
    model = StatsProjectModel
    template_name = "appstats/statsprojectdetail.html"
    slug_field = 'projectcode'
    context_object_name = 'project'

    def dispatch(self, request, *args, **kwargs):
        """
        Parse the current request and save the current project object obtained
        from StatsProjectModel as a global variable accessible from anywhere
        in the class.
        """
        curslug = self.kwargs['slug']
        self.curproject = StatsProjectModel.objects.get(projectcode=curslug)
        return super(StatsProjectView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        SpatiaLite backend does not support `distinct` on `count` query,
        this is a workaround.
        """
        kwargs['mapped_cxt_count'] =\
            ApiFieldsModel.objects.filter(map_id=self.curproject.map_id)\
                .exclude(cxt=None).values('cxt').distinct().count()
        return super(StatsProjectView, self).get_context_data(**kwargs)


class CreateFieldsView(LoginRequiredMixin, CreateView):
    """
    View to create new fields in a map.
    Carries with it a context object to fill the template with already
    existing fields for the selected project (taken by slug).
    """
    model = ApiFieldsModel
    template_name = "appstats/editmap.html"
    slug_field = 'projectcode'
    context_object_name = 'field'
    form_class = ApiFieldsForm

    def dispatch(self, request, *args, **kwargs):
        curslug = self.kwargs['slug']
        self.curproject = StatsProjectModel.objects.get(projectcode=curslug)
        return super(CreateFieldsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['field_list'] = ApiFieldsModel.objects.filter(
            map_id=self.curproject.map_id)
        kwargs['project'] = self.curproject
        return super(CreateFieldsView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        """Automatically defines values for field not showed in the form."""
        form.instance.map = StatsMapModel.objects.get(id=self.curproject.map_id)
        return super(CreateFieldsView, self).form_valid(form)

    def get_success_url(self):
        return reverse('stats_editmap_view',
                       kwargs={'slug': self.kwargs['slug']})


### START test #####################
####################################

class StatsDelfieldView(LoginRequiredMixin, DeleteView):
    model = ApiFieldsModel

    def get_success_url(self):
        return reverse('stats_editmap_view', kwargs={'slug': self.kwargs['slug']})

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

### END test #######################
####################################


class CheckApiStatusView(FormView):
    """Queries API url and returns status"""

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            current_prj = StatsProjectModel.objects.get(
                projectcode=request.POST.get('slug'))
            # check if URL structure is valid
            val = URLValidator()
            try:
                val(str(current_prj.apiurl))
                try:
                    # check if URL is reachable
                    urllib2.urlopen(str(current_prj.apiurl))
                    return HttpResponse('active')
                except urllib2.HTTPError, e:
                    return HttpResponse('')
            except ValidationError, e:
                return HttpResponse('')


class SyncContextView(TemplateView):
    """
    Reads all the contexts from current project's API
    and save them in CxtModel
    """
    def dispatch(self, request, *args, **kwargs):
        """Creates class-wide variable with current project ID"""
        curslug = self.kwargs['slug']
        self.curprojectid = StatsProjectModel.objects.get(
            projectcode=curslug).id
        return super(SyncContextView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Gets data from AJAX POST and recursively add them in the db."""
        if request.is_ajax():
            result = request.POST.get('queryresult')
            js = json.loads(result)
            # iterate on the contexts and save them in the table
            for item in js:
                newcxt = CxtModel(id=int(item), cxt=str(js[item][0:]),
                                  project_id=self.curprojectid)
                newcxt.save()
            return HttpResponse(result)