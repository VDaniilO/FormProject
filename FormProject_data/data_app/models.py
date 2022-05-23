from django.db import models


class FieldModels(models.Model):
    """Models with informations about fields"""
    field_name = models.CharField(max_length=150)
    field_description = models.CharField(max_length=150, blank=True, null=True)
    field_char_type = models.CharField(max_length=350, blank=True, null=True)
    field_text_type = models.TextField(blank=True, null=True)
    field_selec_type = models.TextField(blank=True, null=True)
    form_number = models.ForeignKey('FormModels', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.field_name

class FormModels(models.Model):
    """Models with informations about forms"""
    form_uid = models.IntegerField(db_index=True, unique=True, max_length=6)
    form_name = models.CharField(max_length=150)
    form_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.form_name
