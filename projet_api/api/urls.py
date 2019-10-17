from rest_framework.routers import DefaultRouter
from .apiviews import *
from django.urls import path
from .views import *


router = DefaultRouter()
router.register('Mois', MoisViewSet, base_name='Mois')
router.register('Module', ModuleViewSet, base_name='Module')
router.register('Chapitre', ChapitreViewSet, base_name='Chapitre')
router.register('Cour', CourViewSet, base_name='Cour')

urlpatterns = [
   path('fake_mois', fake_mois, name='fake_mois'),
]

urlpatterns += router.urls