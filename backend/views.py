from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from backend.models import CustomUser
from django.template import loader
from django.http import HttpResponse, JsonResponse

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
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="frontend/login.html", 
        context={'form': form}
        )

# def login(request):
#     if request.user.is_authenticated:
#         return redirect('/')

#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')

#         else:
#             for error in list(form.errors.values()):
#                 print(request, error)

#     form = AuthenticationForm() 

#     template = loader.get_template("frontend/login.html")
#     context = {
#         "lorem": "lorem",
#     }
#     return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template("frontend/register.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))