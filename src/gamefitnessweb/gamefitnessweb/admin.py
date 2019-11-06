from django.contrib import admin

# Register your models here.

from gamefitnessweb.models import Users, Games, Exercises

admin.site.register(Users)
admin.site.register(Games)
admin.site.register(Exercises)
