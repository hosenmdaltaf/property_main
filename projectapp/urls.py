from django.urls import path
from . import views

app_name='projectapp'

urlpatterns = [
    path('', views.project, name='projectpage'),
    path('project_detail/<int:pk>/', views.project_detail, name='project_detailpage'),
    path('loaction_detail/<int:pk>/', views.loaction_detail, name='loaction_detailpage'),

]