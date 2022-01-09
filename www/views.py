from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from www.forms import ContactForm


class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class OfferPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Oferta.html')


class CalendarPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Kalendarz.html')


class BlogPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Blog.html')


class ContactPage(View):

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        ctx = {'form': form }
        return render(request, 'Kontakt.html', ctx)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        ctx = {'form': form }
        if form.is_valid():
            form.save()
            ctx['message'] = 'Dziękuje za kontakt, skontaktuję się z państwem w najbliższym możliwym terminie ;)'
        return render(request, 'Kontakt.html', ctx)


# class ContactPage(SuccessMessageMixin, CreateView):
# form_class = ContactForm
# success_url = reverse_lazy('contact')
# template_name = 'contact/contact.html'
# success_message = "Your message was submitted successfully!"
#
# def form_invalid(self, form):
#     messages.error(self.request, 'Something went wrong with your submission. Please try again.')
#     return HttpResponseRedirect('')
