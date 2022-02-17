from django.shortcuts import render
from projectapp.models import Enquiry,Information,Project
from .models import Slider

def home(request):
    sliders = Slider.objects.all()[:3]
    complated =Project.objects.filter(category='CO')[:4]
    ongoing =Project.objects.filter(category='ON')[:4]
    return render(request,'homeapp/homepage.html',{'complated':complated,'ongoing':ongoing,'sliders':sliders})

def about(request):
    return render(request,'homeapp/about.html')


def landowners(request):
    if request.method == 'POST':
        landowners = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        contact_person = request.POST.get("contact_person")
        land_address = request.POST.get("address")
        property_location = request.POST.get("location")
        type_of_development = request.POST.get("developer")
        special_feature = request.POST.get("feature")
        landowners_requirements  = request.POST.get("note")
        facing = request.POST.get("facing")
        width= request.POST.get("width")
        depth = request.POST.get("depth")

        Information.objects.create(landowners=landowners,contact_person=contact_person,phone=phone,email=email,land_address=land_address,
        property_location=property_location,type_of_development =type_of_development, special_feature=special_feature,
        landowners_requirements=landowners_requirements,facing=facing,width=width,depth=depth)
        return render(request,'global/thankyou.html')
    return render(request,'homeapp/landownerdata.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address= request.POST.get("address")
        message = request.POST.get("message")
        Enquiry.objects.create(name=name,message=message,phone=phone,email=email,
        address=address)
        return render(request,'global/thankyou.html')
    return render(request,'homeapp/contact.html')


def blog(request):
    return render(request,'homeapp/blog.html')

def blog_details(request,pk):
    return render(request,'homeapp/blog_details.html')

def event(request):
    return render(request,'homeapp/events.html')
