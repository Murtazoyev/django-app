from django.shortcuts import render
from django.views.generic import TemplateView


class homePageView(TemplateView):
    template_name = 'home.html'

class aboutePageView(TemplateView):
    template_name = 'aboute.html'

# Create your views here.
