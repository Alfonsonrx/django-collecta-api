from django.contrib import admin
from .models import Category, SubCategory, Miniature, MiniatureImage

# Register your models here.
admin.site.register([Category, SubCategory, Miniature, MiniatureImage])