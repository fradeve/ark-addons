__appname__ = "stats"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

import urllib2

from django.views.generic import ListView, CreateView, DetailView, FormView,\
    TemplateView
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from braces.views import LoginRequiredMixin

from .models import StatsProjectModel


class IndexView(TemplateView):
    template_name = "index.html"


class ManageProjectsView(LoginRequiredMixin, ListView):
    template_name = "statsprojects.html"
    model = StatsProjectModel


class StatsCreateView(LoginRequiredMixin, CreateView):
    """Creates a new instance using StatsProjectModel model"""
    template_name = "addproject.html"
    model = StatsProjectModel


class StatsProjectView(LoginRequiredMixin, DetailView):
    """Returns a view with project's details"""
    model = StatsProjectModel
    template_name = "statsprojectdetail.html"
    slug_field = 'projectcode'
    context_object_name = 'object'


class CheckApiStatusView(FormView):
    """Queries API url and returns status"""

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            current_prj = StatsProjectModel.objects.get(projectcode=request.POST.get('slug'))
            # first, check if URL structure is valid
            val = URLValidator()
            try:
                val(str(current_prj.apiurl))
                try:
                    # check if URL is online
                    urllib2.urlopen(str(current_prj.apiurl))
                    return HttpResponse('active')
                except urllib2.HTTPError, e:
                    print(e.code)
                    return HttpResponse('')
            except ValidationError, e:
                print(e)
                return HttpResponse('')