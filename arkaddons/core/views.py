from django.views.generic import ListView, TemplateView, CreateView, DetailView, FormView
from django.http import HttpResponse
from braces.views import LoginRequiredMixin

import MySQLdb

from .models import ArkProjectModel

class IndexView(TemplateView):
    template_name = "index.html"

class ManageProjectsView(LoginRequiredMixin, ListView):
    template_name = "projects.html"
    model = ArkProjectModel

class ArkCreateView(LoginRequiredMixin, CreateView):
    """Creates a new instance using ArkProjectModel model"""
    template_name = "addproject.html"
    model = ArkProjectModel

class ArkProjectView(LoginRequiredMixin, DetailView):
    model = ArkProjectModel
    template_name = "projectdetail.html"
    slug_field = 'projectslug'
    context_object_name = 'object'

# when listing table fields, this might be useful
# http://django-inspect-model.readthedocs.org
# http://stackoverflow.com/questions/6585373/django-multiple-and-dynamic-databases

class CheckDbStatusView(FormView):

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            current_prj = ArkProjectModel.objects.get(projectslug=request.POST.get('slug'))
            try:
                db = MySQLdb.connect(host=str(current_prj.arkdbhost),
                                     user=str(current_prj.arkdbuser),
                                     passwd=str(current_prj.arkdbpassword),
                                     db=str(current_prj.arkdbname),
                                     port=int(current_prj.arkdbport))
                return HttpResponse('active')
            except:
                return HttpResponse('')

