from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('main/', form_out, name='all-form'),
    path('main/add_form', add_form, name='add-form'),
    path('main/edit_form/<int:form_uid>', edit_form, name='edit-form'),
    path('main/add_fields/', add_field, name='add-fields')
]
