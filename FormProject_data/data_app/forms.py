from django import forms

from .models import *


class CreateForm(forms.ModelForm):
    class Meta:
        model = FormModels
        fields = ['form_uid', 'form_name']

class CreateFieldForm(forms.ModelForm):
    class Meta:
        model = FieldModels
        fields = ['field_name', 'field_description', 'field_char_type', 'field_text_type', 'field_selec_type', 'form_number']
