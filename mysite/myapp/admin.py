from django.contrib import admin
from .models import Flower, Category,Tag
# Register your models here.

admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Tag)
