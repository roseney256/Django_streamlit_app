from django.shortcuts import render
from personal.models import Question
from account.models import Account

# Create your views here.

def home_screen_views(request):

    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts


    return render(request, "personal/home.html", context)

def landing_screen_views(request):

    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts


    return render(request, "personal/landing.html", context)

def dashboard_screen_views(request):

    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts


    return render(request, "personal/dashboard.html", context)

def highres_views(request):

    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts


    return render(request, "personal/highres.html", context)

def about_views(request):

    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts


    return render(request, "personal/about.html", context)