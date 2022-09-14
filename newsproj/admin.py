from django.contrib import admin
from .models import Category, New, NewCategory


admin.site.register(Category)
admin.site.register(New)
admin.site.register(NewCategory)