from django.contrib import admin
from .models import CustomUser, Organization, Event, Image, Jedzenie, Usluga, Przedmiot

admin.site.register(CustomUser)
admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Image)
admin.site.register(Jedzenie)
admin.site.register(Usluga)
admin.site.register(Przedmiot)