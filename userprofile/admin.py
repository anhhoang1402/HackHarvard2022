from django.contrib import admin
from .models import userPref
from .models import userRec

# Register your models here.
admin.site.register(userPref)
admin.site.register(userRec)