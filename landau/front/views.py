from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'index.html'

class TablePage(TemplateView):
    template_name = 'table.html'
