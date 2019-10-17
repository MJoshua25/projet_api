from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from .models import *


class CourSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Cour
        fields = '__all__'


class ChapitreSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    cours = CourSerializer(many=True, required=False)

    class Meta:
        model = Chapitre
        fields = '__all__'


class ModuleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    chapitres = ChapitreSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Module
        fields = '__all__'


class MoisSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    Modules = ModuleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Mois
        fields = '__all__'