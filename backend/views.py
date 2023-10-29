from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from backend.forms import FormJedzenie, FormOrganizationCreate, FormPrzedmiot, FormUserRegistration, FormUsluga
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout

from backend.models import CustomUser, Jedzenie, Organization, Przedmiot, Usluga, Event

def is_admin(user):
    return user.is_superuser


def index(request):
    template = loader.get_template("frontend/index.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))

def organizacja_form(request):
    template = loader.get_template("frontend/organizacja_form.html")
    form = FormOrganizationCreate()
    context = {
        "lorem": "lorem",
        "form": form,
    }
    
    return HttpResponse(template.render(context, request))


def sharefood(request):
    user = request.user
    if user.is_authenticated:
        rola = user.rola
    else: 
        rola = None
    if rola == "POTRZEBUJACY":
        jedzenie = Jedzenie.objects.all()
        return render(request, 'frontend/sharefood.html', {'jedzenie': jedzenie, 'rola': rola})
    elif rola == 'WOLONTARIUSZ':
        form = FormJedzenie()
        dodane_jedzenie = user.jedzenie.all()
        return render(request, 'frontend/sharefood.html', {'form': form, 'rola': rola, 'dodane_jedzenie': dodane_jedzenie})
    else:
        pass
    
    template = loader.get_template("frontend/sharefood.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def shareitems(request):
    user = request.user
    if user.is_authenticated:
        rola = user.rola
    else: 
        rola = None
    if rola == "POTRZEBUJACY":
        przedmiot = Przedmiot.objects.all()
        return render(request, 'frontend/shareitems.html', {'przedmiot': przedmiot, 'rola': rola})
    elif rola == 'WOLONTARIUSZ':
        form = FormPrzedmiot()
        dodane_przedmioty = user.przedmiot.all()
        return render(request, 'frontend/shareitems.html', {'form': form, 'rola': rola, 'dodane_przedmioty': dodane_przedmioty})
    else:
        pass

    template = loader.get_template("frontend/shareitems.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def shareskills(request):
    user = request.user
    if user.is_authenticated:
        rola = user.rola
    else: 
        rola = None
    if rola == "POTRZEBUJACY":
        usluga = Usluga.objects.all()
        return render(request, 'frontend/shareskills.html', {'usluga': usluga, 'rola': rola})
    elif rola == 'WOLONTARIUSZ':
        form = FormUsluga()
        dodane_uslugi = user.usluga.all()
        return render(request, 'frontend/shareskills.html', {'form': form, 'rola': rola, 'dodane_uslugi':dodane_uslugi})
    else:
        pass

    template = loader.get_template("frontend/shareskills.html")
    context = {
        "lorem": "lorem",
    }
    return HttpResponse(template.render(context, request))


def events(request):
    events = Event.objects.all()
    template = loader.get_template("frontend/events.html")
    context = {
        "events": events,
    }
    return HttpResponse(template.render(context, request))

def fundacje(request):
    user = request.user
    twoje_organizacje = user.organizacja.all()
    inne_organizacje = Organization.objects.exclude(id__in=twoje_organizacje.values_list('id', flat=True))

    return render(
        request = request,
        template_name = "frontend/fundacje.html",
        context={"twoje_organizacje":twoje_organizacje, "inne_organizacje":inne_organizacje}
        )


def account(request):
    template = loader.get_template("frontend/account.html")
    context = {
        "username": request.user.username,
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

    nowyUser = CustomUser.objects.create(first_name=firstName, last_name=lastName, username=username, telefon=telefon, email=email, password=haszPassword)
    nowyUser.save()

    return HttpResponse('Stworzono nowego użytkownika')

def food_update(request, foodId):
    food = get_object_or_404(Jedzenie, food_id=foodId)
    food_id = food.food_id
    form = FormJedzenie(instance=food)

    return render(
        request = request,
        template_name = "frontend/food_update.html",
        context={"form":form, "food_id":food_id}
        )


def item_update(request, itemId):
    item = get_object_or_404(Przedmiot, item_id=itemId)
    item_id = item.item_id
    form = FormJedzenie(instance=item)

    return render(
        request = request,
        template_name = "frontend/item_update.html",
        context={"form":form, "item_id":item_id}
        )


def skill_update(request, skillId):
    skill = get_object_or_404(Usluga, service_id=skillId)
    skill_id = skill.service_id
    form = FormJedzenie(instance=skill)

    return render(
        request = request,
        template_name = "frontend/skill_update.html",
        context={"form":form, "skill_id":skill_id}
        )
# AJAX


# @ensure_csrf_cookie
def AjaxCreateFood(request):
    food_name = request.POST['food_name']
    food_description = request.POST['food_description']
    food_image = request.FILES['food_image']

    user = request.user
    food = Jedzenie.objects.create(uzytkownik=user.email, food_name=food_name, food_description=food_description, food_image=food_image)
    food.save()
    print(user.jedzenie)
    user.jedzenie.add(food)
    return JsonResponse({'msg':'File successfully uploaded'})

def AjaxCreateItem(request):
    item_name = request.POST['item_name']
    item_description = request.POST['item_description']
    item_image = request.FILES['item_image']

    user = request.user
    item = Przedmiot.objects.create(uzytkownik=user.email, item_name=item_name, item_description=item_description, item_image=item_image)
    item.save()
    user.przedmiot.add(item)
    return JsonResponse({'msg':'File successfully uploaded'})

def AjaxCreateSkill(request):
    service_name = request.POST['service_name']
    service_description = request.POST['service_description']
    service_price = request.POST['service_price']
    service_image = request.FILES['service_image']

    user = request.user
    skill = Usluga.objects.create(uzytkownik=user.email, service_name=service_name, service_description=service_description, service_price=service_price, service_image=service_image)
    skill.save()

    user.usluga.add(skill)
    return JsonResponse({'msg':'File successfully uploaded'})

def AjaxCreateOrganization(request):
    nazwa = request.POST['nazwa']
    opis = request.POST['opis']
    logo = request.FILES['logo']


    user = request.user
    organizacja = Organization.objects.create(uzytkownik=user.email, nazwa=nazwa, opis=opis, logo=logo)
    organizacja.save()

    user.organizacja.add(organizacja)
    return JsonResponse({'msg':'File successfully uploaded'})

    # return HttpResponse('Stworzono jedzenie')

    # superusers = CustomUser.objects.filter(is_superuser=True)
    # if request.user.is_superuser:
    #     form = AdminOrderForm(request.POST, request.FILES)
    #     users = request.POST.getlist('uzytkownik', None)
    # else:
    #     form = OrderForm(request.POST, request.FILES)
    # files = request.FILES.getlist('files[]', None)
    # order = form.save(commit=False)
    # order.save()
    # zalaczniki_publiczne = []
    # if request.user.is_superuser:
    #     order.uzytkownik.add(*users)
    #     order.save()
    # else:
    #     order.uzytkownik.add(request.user)
    #     order.save()
    # for file in files:
    #     zalacznik = OrderZalacznikPubliczne.objects.create(zalacznikPubliczne=file)
    #     zalaczniki_publiczne.append(zalacznik)
    # uwagaPubliczna = UwagiPubliczne.objects.create(uzytkownik=request.user, order=order, trescPubliczne="Stworzono zlecenie")
    # uwagaPubliczna.save()
    # uwagaPubliczna.zalacznikiPubliczne.add(*zalaczniki_publiczne)
    # if request.user.is_superuser: 
    #     for user in users:
    #         existing_user = get_object_or_404(CustomUser, id=user)
    #         createStatus = OrderStatus.objects.create(uzytkownik=existing_user, order=order, status="DO_WYKONANIA")
    #         createStatus.save()  
    # else:
    #     for superUser in superusers:
    #         createStatus = OrderStatus.objects.create(uzytkownik=superUser, order=order, status="DO_WYKONANIA")
    #         createStatus.save()
    # createStatus = OrderStatus.objects.create(uzytkownik=request.user, order=order, status="DO_WYKONANIA")
    # createStatus.save()
    # addAllUsers(order.id,request.user)
    # users_list = order.uzytkownik.all()
    # users_email_list=[]
    # for user in users_list:
    #     users_email_list.append(user.email)
    # if(order.nr_zlecenia!=""):
    #     message = "Stworzono nowe zlecenie o numerze "+order.nr_zlecenia+"."
    # else:
    #     message = "Stworzono nowe zlecenie."

    # # t = threading.Thread(target=sending, args=(request, users_email_list, 'Stworzono zlecenie', message))
    # # t.start()
    # sending(request, users_email_list, 'Stworzono zlecenie', message)
    # return JsonResponse({'msg':'<span style="color: green;">File successfully uploaded</span>'})

def AjaxUpdateFood(request):
    food_name = request.POST.get('food_name')
    food_description = request.POST.get('food_description')
    food_id = request.POST.get('food_id')
    food_image = request.POST.get['food_image']
    # food_image = request.POST.get('food_image')
    food = get_object_or_404(Jedzenie, food_id=food_id)
    food.food_name = food_name
    food.food_description = food_description
    food.food_image = food_image
    food.save()
    return JsonResponse({'msg':'File successfully uploaded'})

def AjaxUpdateItem(request):
    item_name = request.POST.get('foitem_nameod_name')
    item_description = request.POST.get('item_description')
    item_id = request.POST.get('item_id')
    item_image = request.POST.get('item_image')
    item = get_object_or_404(Przedmiot, item_id=item_id)
    item.item_name = item_name
    item.item_description = item_description
    item.item_image = item_image
    item.save()
    return JsonResponse({'msg':'File successfully uploaded'})

def AjaxUpdateSkill(request):
    service_name = request.POST.get('service_name')
    service_description = request.POST.get('service_description')
    service_id = request.POST.get('service_id')
    service_price = request.POST.get('service_price')
    service_image = request.POST.get('service_image')
    skill = get_object_or_404(Usluga, service_id=service_id)
    skill.service_name = service_name
    skill.service_description = service_description
    skill.service_price = service_price
    skill.service_image = service_image
    skill.save()
    return JsonResponse({'msg':'File successfully uploaded'})