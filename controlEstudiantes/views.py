from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

def base(request):
    return render(request, 'controlEstudiantes/base.html', {})
