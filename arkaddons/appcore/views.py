__appname__ = "appcore"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.views.generic import CreateView, ListView, DetailView,\
    TemplateView, FormView
from django.http import HttpResponse

from braces.views import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import link
import MySQLdb
from _mysql_exceptions import OperationalError

from .models import ArkProjectModel
from .arkmodels import CxtTblCxt
from .serializers import CxtSerializer


class IndexView(TemplateView):
    template_name = "index.html"


class ManageProjectsView(LoginRequiredMixin, ListView):
    template_name = "appcore/projects.html"
    model = ArkProjectModel


class ArkCreateView(LoginRequiredMixin, CreateView):
    """Creates a new instance using ArkProjectModel model"""
    template_name = "addproject.html"
    model = ArkProjectModel


class ArkProjectView(LoginRequiredMixin, DetailView):
    model = ArkProjectModel
    template_name = "appcore/projectdetail.html"
    slug_field = 'projectslug'
    context_object_name = 'object'


class CheckDbStatusView(FormView):
    """Queries API url and returns status"""

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            current_prj = ArkProjectModel.objects.get(
                projectslug=request.POST.get('slug'))
            try:
                db = MySQLdb.connect(host=str(current_prj.arkdbhost),
                                     user=str(current_prj.arkdbuser),
                                     passwd=str(current_prj.arkdbpassword),
                                     db=str(current_prj.arkdbname),
                                     port=int(current_prj.arkdbport))
                return HttpResponse('active')
            except OperationalError:
                return HttpResponse('')


class CxtOneViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = CxtTblCxt.objects.all()
        serializer_class = CxtSerializer

        def get_queryset(self):
            cur_project = self.kwargs['slug']
            return CxtTblCxt.objects.using(cur_project)


class CxtAllViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CxtTblCxt.objects.using('ark_arktest').all()
    serializer_class = CxtSerializer


class RetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CxtTblCxt.objects.using('ark_arkprescot2').all()
    serializer_class = CxtSerializer

    @link()
    def detail(self, request):
        #queryset = CxtTblCxt.objects.using('ark_' + request.POST.get('slug')).all()
        queryset = CxtTblCxt.objects.all()
        serializer = CxtSerializer(queryset)
        return Response(serializer.data)