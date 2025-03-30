from django.urls import path
from  . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('kontak/', views.contact, name='contact'),
    
]
