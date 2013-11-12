from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView
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

class ArkProjectEdit(LoginRequiredMixin, UpdateView): #FIXME
    """Creates a new instance using ArkProjectModel model"""
    template_name = "projectedit.html"
    model = ArkProjectModel
    context_object_name = 'object'

class ArkProjectView(LoginRequiredMixin, DetailView):
    model = ArkProjectModel
    template_name = "projectdetail.html"
    slug_field = 'projectslug'
    context_object_name = 'object'

#class ArkProjectImport(LoginRequiredMixin):

# when listing table fields, this might be useful
# http://django-inspect-model.readthedocs.org
# http://stackoverflow.com/questions/6585373/django-multiple-and-dynamic-databases

def checkdbstatus(request):
    if request.is_ajax():
        if request.method == ('POST'):
            CurrentPrj = ArkProjectModel.objects.filter(projectslug=request.POST.get('slug'))[0]
            try:
                db = MySQLdb.connect(host=str(CurrentPrj.arkdbhost),
                                     user=str(CurrentPrj.arkdbuser),
                                     passwd=str(CurrentPrj.arkdbpassword),
                                     db=str(CurrentPrj.arkdbname),
                                     port=int(CurrentPrj.arkdbport))
                return HttpResponse('active')
            except:
                return HttpResponse('')
