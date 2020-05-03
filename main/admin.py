from django.contrib import admin
from main import models

# Register your models here.

admin.site.register(models.Keyword)
admin.site.register(models.Post)
admin.site.register(models.Nation)