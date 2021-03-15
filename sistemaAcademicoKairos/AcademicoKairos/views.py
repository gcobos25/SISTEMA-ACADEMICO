from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from AcademicoKairos.models import ConfiguracionUsuario
from templates import loginconf
# Create your views here.

class LoginInit(auth_views.LoginView):
	template_name = 'loginconf/login.html'
