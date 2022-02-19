from turtle import width
from django.shortcuts import render

from projectapp.models import Project,Enquiry


def project(request):
    projects = Project.objects.all()
    commercial =Project.objects.filter(category='CM')
    ongoing =Project.objects.filter(category='ON')
    complated =Project.objects.filter(category='CO')
   
    # print('--------------------------')
    # all=[]
    # a=[x for x in projects]
    # for to in a:
    #     done = to.short_loaction 
    #     all.append(done) 
    # print(all)
    # print('---------------------------')
    return render(request,'projectapp/project.html',{'commercial':commercial,'ongoing':ongoing,'complated':complated,
    'projects':projects,'all':all})

def project_detail(request,pk):
    object =Project.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address= request.POST.get("address")
        message = request.POST.get("message")
        Enquiry.objects.create(name=name,message=message,phone=phone,email=email,
        address=address)
        return render(request,'global/thankyou.html')

    return render (request,'projectapp/project_detail.html',{'object':object})

def loaction_detail(request,pk):
    loaction =Project.objects.filter(short_loaction=pk)
    print(loaction)
    return render (request,'projectapp/loaction.html',{'loaction':loaction})
