from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("frontend/index.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))