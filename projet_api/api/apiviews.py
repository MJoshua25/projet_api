from rest_framework import viewsets,filters

from .models import *
from .serializers import *

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class MoisViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Mois.objects.all()
    serializer_class = MoisSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ChapitreViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer

class CourViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Cour.objects.all()
    serializer_class = CourSerializer