from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


    
class Organization(models.Model):
    nazwa = models.CharField(max_length=50, blank=False)
    uzytkownik = models.CharField(max_length=100, blank=True)
    opis = models.CharField(max_length=500, blank=True)
    logo = models.ImageField(upload_to='documents/', blank=True)


TITLE_CHOICES = [
    ('Sportowe', 'Sportowe'),
    ('Kulturowe', 'Kulturowe'),
    ('Rozrywkowe', 'Rozrywkowe'),
]

class Event(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    creator_id = models.ManyToManyField(Organization, blank=True)
    event_name = models.CharField(max_length=100, blank=True)
    event_description = models.CharField(max_length=500, blank=True)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=100, blank=True)
    type_of_event = models.CharField(max_length=30, choices=TITLE_CHOICES, blank=True, null=True)
    main_image = models.ImageField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    link_do_miejsca_wydarzenia =  models.URLField(max_length = 200, blank=True, null=True)
    x_miejsca = models.FloatField(null=True)
    y_miejsca = models.FloatField(null=True)


class Image(models.Model):
    event = models.ForeignKey(Event, default=None, related_name='events', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='documents/')
    def __str__(self):
        return self.event.event_name
    

class Jedzenie(models.Model):
    food_id = models.BigAutoField(primary_key=True)
    uzytkownik = models.CharField(max_length=100, blank=True)
    food_name = models.CharField(max_length=100, blank=True)
    food_description = models.CharField(max_length=100, blank=True)
    food_image = models.ImageField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

class Przedmiot(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    uzytkownik = models.CharField(max_length=100, blank=True)
    item_name = models.CharField(max_length=100, blank=True)
    item_description = models.CharField(max_length=100, blank=True)
    item_image = models.ImageField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

class Usluga(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    uzytkownik = models.CharField(max_length=100, blank=True)
    service_name = models.CharField(max_length=100, blank=True)
    service_description = models.CharField(max_length=100, blank=True)
    service_price = models.CharField(max_length=100, blank=True)
    service_image = models.ImageField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)


ROLA = [
        ("POTRZEBUJACY", "Potrzebujący"),
        ("WOLONTARIUSZ", "Wolontariusz"),
    ]

class CustomUser(AbstractUser):
    telefon = models.CharField(max_length=30, blank=True)
    adres_zamieszkania = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, blank=True)
    data_urodzenia = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='documents/', blank=True)
    rola = models.CharField(max_length=30, choices=ROLA, blank=True)
    zweryfikowany = models.BooleanField(blank=True, null=True)
    jedzenie = models.ManyToManyField(Jedzenie, blank=True)
    usluga = models.ManyToManyField(Usluga, blank=True)
    przedmiot = models.ManyToManyField(Przedmiot, blank=True)
    organizacja = models.ManyToManyField(Organization, blank=True)
    # avatar = models.ImageField(blank=True, default="images/1.png")

    def __str__(self):
        return self.email