from django.contrib import admin

from .models import CustomUser,Course
    
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Course)


