from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from backend.forms import FormJedzenie, FormUserRegistration
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout

from backend.models import CustomUser, Jedzenie

def is_admin(user):
    return user.is_superuser


def index(request):
    template = loader.get_template("frontend/index.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def sharefood(request):
    user = request.user
    rola = user.rola
    if rola == "POTRZEBUJACY":
        jedzenie = Jedzenie.objects.all()
        return render(request, 'frontend/sharefood.html', {'jedzenie': jedzenie, 'rola': rola})
    elif rola == 'WOLONTARIUSZ':
        form = FormJedzenie()
        return render(request, 'frontend/sharefood.html', {'form': form, 'rola': rola})
    else:
        pass
    
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





# UŻYTKOWNIK
def logout_view(request):
    logout(request)
    return redirect('/')

def web_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/login')

    form = AuthenticationForm()
    form.fields['username'].label = 'Login:'
    form.fields['password'].label = 'Hasło:'

    return render(
        request=request,
        template_name="frontend/login.html",
        context={'form': form}
        )



def register(request):
    form = FormUserRegistration()

    return render(
        request = request,
        template_name = "frontend/register.html",
        context={"form":form}
        )

def createUser(request):
    print("1231231")
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    username = request.POST['username']
    telefon = request.POST['telefon']
    email = request.POST['email']
    password = request.POST['passwordFirst']
    haszPassword = make_password(password)
    print("START")
    nowyUser = CustomUser.objects.create(first_name=firstName, last_name=lastName, username=username, telefon=telefon, email=email, password=haszPassword)
    nowyUser.save()
    print("END")
    return HttpResponse('Stworzono nowego użytkownika')
