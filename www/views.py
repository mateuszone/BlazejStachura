from calendar import Calendar
from datetime import timedelta, datetime, date
import calendar
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import View, generic
from django.views.generic import CreateView, ListView

from www.forms import ContactForm, EventForm
from www.models import Event
from www.utils import Calendar


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
        ctx = {'form': form}
        return render(request, 'Kontakt.html', ctx)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            form.save()
            ctx['message'] = 'Dziękuje za kontakt, skontaktuję się z państwem w najbliższym możliwym terminie ;)'
        return render(request, 'Kontakt.html', ctx)


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


# class CalendarView(generic.ListView):
#     model = Event
#     template_name = "Kalendarz.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get("month", None))
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context["calendar"] = mark_safe(html_cal)
#         context["prev_month"] = prev_month(d)
#         context["next_month"] = next_month(d)
#         return context


class CalendarView(View):

    def get(self, request, *args, **kwargs):
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context = {}
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return render(request, 'Kalendarz.html', context)
