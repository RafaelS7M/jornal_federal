from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class NoticiaPageView(TemplateView):
    template_name = 'noticia.html'

class MatriculaPageView(TemplateView):
    template_name = 'login.html'