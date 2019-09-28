from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.forms import ModelForm
from django.db import models


# class User(models.Model):
#     userid = models.CharField(max_length=30)
#     # triage = models.CharField(max_length=30)
#
#
# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['userid']


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    return render(request, '../templates/login.html')


def register(request):
    if request.method == 'POST':  # If the form has been submitted...
        user = request.POST.get('user_id')
        # return HttpResponse(user)
        return render(request, '../templates/home.html')
    else:
        return HttpResponse("not registered")
