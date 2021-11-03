from django.contrib import admin

from myapp import models
from . models import Feature
# Register your models here.

admin.site.register(Feature)