from django.contrib import admin
from .models import Slider,Blog,Events

# Register your models here.

admin.site.register(Slider)

class  Bloglist(admin.ModelAdmin):
    list_display = ('name','thumnail_img')

admin.site.register(Blog, Bloglist)

class  Eventlist(admin.ModelAdmin):
    list_display = ('name','image')

admin.site.register(Events, Eventlist)