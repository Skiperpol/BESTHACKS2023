from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("frontend/index.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def sharefood(request):
    template = loader.get_template("frontend/sharefood.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def shareitems(request):
    template = loader.get_template("frontend/shareitems.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def shareskills(request):
    template = loader.get_template("frontend/shareskills.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def events(request):
    template = loader.get_template("frontend/events.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))

def fundacje(request):
    template = loader.get_template("frontend/fundacje.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("frontend/login.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template("frontend/register.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))