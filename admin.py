from django.contrib import admin
# Register your models here.
from .models import profile, userStripe

admin.site.register(profile)
admin.site.register(userStripe)