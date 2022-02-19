
from email import message
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from django.conf import settings

from homeapp.compress import compress



class Category(models.Model):
    name = models.CharField(max_length=200,help_text="name of the project category")

    def __str__(self):
        return str(self.name)

CATEGORY_CHOICES = (
("ON", "Ongoing"),
("CM", "Commercial"),
("CO", "Complated"),)

class Project(models.Model):

    name = models.CharField(max_length=200,help_text="name of the project")
    # categories = models.ForeignKey(Category,on_delete=models.CASCADE, null=True,blank=True,help_text="name of the project category")

    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2,null=True,blank=True)

    thumnail_image = models.ImageField(upload_to='project_img-thumnails')

    short_loaction = models.CharField(max_length=150,null=True,blank=True,
    help_text="short loaction:example:uttara/Gulshan etc.")

    apartment_type = models.TextField(max_length=500,null=True,blank=True,
    help_text="type of apartments -->example:12 storey luxury 4 bedroom apartments")

    detail_loaction = models.TextField(null=True,blank=True,
    help_text="detail_loactions -->example:House 4A, Road 67,Gulshan")

    availability= models.CharField(max_length=200,help_text="Sale complete/or not")

    apartment_size = models.IntegerField(help_text='apartment_size in sft')

    handover = models.CharField(max_length=150,null=True,blank=True,
    help_text="handover date ---->:example:December, 2021.")

    total_apartments = models.IntegerField(help_text='how many apartment--->example:20/10 etc')

    features = RichTextUploadingField(help_text='features of apartment', null = True, blank = True)

    # loaction_map = models.URLField(help_text='loaction map url of your project',null=True,blank=True)

    loaction_maptxt = models.CharField(max_length=255,
    help_text='loaction map url of your project',null=True,blank=True)

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.thumnail_img)
        # set self.image to new_image
        self.thumnail_img = new_image
        # save
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    def image_tag(self):
        if self.thumnail_image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.thumnail_image))

class Projectimages(models.Model):
    case = models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)

    images = models.ImageField(upload_to='project_images',null=True,blank=True)

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.images)
        # set self.image to new_image
        self.images = new_image
        # save
        super().save(*args, **kwargs)


class Enquiry(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True,)
    address = models.TextField(null=True,blank=True,)
    phone = models.CharField(max_length=100,null=True,blank=True,)
    email = models.EmailField(null=True,blank=True,)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)



class Information(models.Model):
    landowners = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    contact_person = models.CharField(max_length=255,null=True,blank=True) 
    land_address = models.TextField(null=True,blank=True)
    property_location = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    type_of_development = models.CharField(max_length=255,null=True,blank=True)
    special_feature = models.TextField(null=True,blank=True)
    landowners_requirements = models.TextField(null=True,blank=True)
    facing = models.CharField(max_length=255,null=True,blank=True)

    # land_area = models.CharField(max_length=255,null=True,blank=True)
    # land_dimension = models.CharField(max_length=255,null=True,blank=True)
    width = models.CharField(max_length=255,null=True,blank=True)
    depth = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.landowners)
