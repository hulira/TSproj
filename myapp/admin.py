from django.contrib import admin
from .import models

# Register your models here.
from .models import Staff_Details

admin.site.register(Staff_Details)
