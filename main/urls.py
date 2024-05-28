from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='index'),
    path('about/<int:pk>/', views.magazine_details, name='about'),
    path('like/<int:pk>/', views.like_request, name='like'),

]
