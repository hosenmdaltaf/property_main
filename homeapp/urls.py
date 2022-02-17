from django.urls import path
from . import views

app_name='homeapp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name='aboutpage'),
    path('landowner', views.landowners, name='landownerpage'),
    path('contact/', views.contact, name='contactpage'),
    path('blog/', views.blog, name='blogpage'),
    path('blog/<int:pk>/', views.blog_details, name='blogdetailpage'),
    path('event/', views.event, name='eventpage'),
]