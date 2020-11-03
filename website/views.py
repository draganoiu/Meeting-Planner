from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting


# Create your views here.


def welcome(request):
    return render(request, 'website/welcome.html',
                  {'meetings': Meeting.objects.all()})


def date(request):
    return HttpResponse('This page was ..')


def abouta(request):
    return HttpResponse('about page')
