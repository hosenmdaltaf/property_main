from django.db import models
from django.utils.html import mark_safe
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

from homeapp.compress import compress


# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to="slider_image")

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)

class Events(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to="event_image",null=True,blank=True)
    content = RichTextUploadingField(null=True,blank=True)

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)

    def __str_(self):
       return str(self.name) 

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))



class Blog(models.Model): 
    name = models.TextField()
    thumnail_img = models.ImageField(upload_to='blog_thumnail_img',null=True,blank=True)
    content = RichTextUploadingField(null=True,blank=True)

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.thumnail_img)
        # set self.image to new_image
        self.thumnail_img = new_image
        # save
        super().save(*args, **kwargs)

    def __str_(self):
       return str(self.name)

    def image_tag(self):
        if self.thumnail_image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.thumnail_image))


