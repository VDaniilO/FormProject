from rest_framework import serializers

from .models import FieldModels, FormModels


class FormsFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldModels
        fields = "__all__"

class FormsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormModels
        fields = "__all__"
