from django.contrib import admin
from .models import CustomUser, Organization, Event, Image

admin.site.register(CustomUser)
admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Image)
