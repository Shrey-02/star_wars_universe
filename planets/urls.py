from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('detail/<int:planet_id>', views.detail, name='detail'),
   
    
]