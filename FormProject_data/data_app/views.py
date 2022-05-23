from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics, viewsets

from .forms import CreateForm, CreateFieldForm
from .models import *
from .serializers import FormsFieldSerializer, FormsSerializer

def form_out(request):
    get_form = FormModels.objects.all()
    context = {
        'get_form': get_form,
    }
    return render(request, "data_app/index.html", context)


def edit_form(request, form_number):
    get_feilds = FieldModels.objects.all()
    num = form_number
    context = {
        'get_feilds': get_feilds,
        'num': num,
    }
    return render(request, "data_app/form_edit.html", context)


def add_form(request):
    if request.method == 'POST':
        form_add = CreateForm(request.POST)
        if form_add.is_valid():
            FormModels.objects.create(**form_add.cleaned_data)
            return redirect('all-form')
    else:
        form_add = CreateForm()

    return render(request, "data_app/add_form.html", {'form_add': form_add})


def add_field(request):
    if request.method == 'POST':
        fields_add = CreateFieldForm(request.POST)
        if fields_add.is_valid():
            FieldModels.objects.create(**fields_add.cleaned_data)
            return redirect('all-form')
    else:
        fields_add = CreateFieldForm()

    return render(request, "data_app/add_fields.html", {'fields_add': fields_add})


class FormAPIList(generics.ListCreateAPIView):

    queryset = FieldModels.objects.all()
    serializer_class = FormsFieldSerializer


class FormAPIUpdate(generics.RetrieveUpdateAPIView):

    queryset = FormModels.objects.all()
    serializer_class = FormsSerializer
    lookup_field = 'form_number'
