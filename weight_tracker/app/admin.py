from django.contrib import admin

# Register your models here.

from .models import User, Weight
admin.site.register(User)
admin.site.register(Weight)