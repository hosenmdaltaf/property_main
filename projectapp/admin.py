from django.contrib import admin

from .models import Project,Category,Projectimages,Enquiry,Information

admin.site.register(Category)

class ProjectImageAdmin(admin.StackedInline):
    model = Projectimages

class Projectlist(admin.ModelAdmin):
    list_display = ('name','category','image_tag','short_loaction','apartment_type','availability','apartment_size'
    ,'handover','total_apartments','detail_loaction')
    inlines = [ProjectImageAdmin]

admin.site.register(Project,Projectlist)


class  Enquirylist(admin.ModelAdmin):
    list_display = ('name','phone','email','address','message')

admin.site.register(Enquiry, Enquirylist)

class  Informationlist(admin.ModelAdmin):
    list_display = ('landowners','contact_person','phone','email','land_address','width','depth','property_location',
    'type_of_development','special_feature','landowners_requirements','facing')

admin.site.register(Information, Informationlist)