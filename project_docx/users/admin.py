from django.contrib import admin
from .models import Saved, CustomUser
from django.contrib.auth.models import Group
# Register your models here.


admin.site.unregister(Group)
admin.site.register(Saved)
admin.site.register(CustomUser)