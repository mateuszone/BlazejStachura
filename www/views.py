from django.shortcuts import render

# Create your views here.
from django.views import View


class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ContactPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Kontakt.html')
