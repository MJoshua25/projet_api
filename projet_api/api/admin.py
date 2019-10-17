from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MoisAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'cover',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = ('date_add', 'date_up', 'status')


class ModuleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'mois',
        'langage',
        'image',
        'description',
        'prix',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
        'date_add',
        'date_up',
        'status',
        'id',
        'mois',
        'langage',
        'image',
        'description',
        'prix',
        'date_add',
        'date_up',
        'status',
    )
    raw_id_fields = ('mois',)


class ChapitreAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'module',
        'titre',
        'description',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
        'module',
        'date_add',
        'date_up',
        'status',
        'id',
        'module',
        'titre',
        'description',
        'date_add',
        'date_up',
        'status',
    )


class CourAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'chapitre',
        'titre',
        'video',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
        'chapitre',
        'date_add',
        'date_up',
        'status',
        'id',
        'chapitre',
        'titre',
        'video',
        'date_add',
        'date_up',
        'status',
    )


class User_CourseAdmin(admin.ModelAdmin):

    list_display = ('id', 'module', 'user', 'date_add', 'date_up', 'status')
    list_filter = (
        'module',
        'user',
        'date_add',
        'date_up',
        'status',
        'id',
        'module',
        'user',
        'date_add',
        'date_up',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Mois, MoisAdmin)
_register(models.Module, ModuleAdmin)
_register(models.Chapitre, ChapitreAdmin)
_register(models.Cour, CourAdmin)
_register(models.User_Course, User_CourseAdmin)
