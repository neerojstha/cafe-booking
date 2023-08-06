from . import views
from .views import booking, menu
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('booking/', views.booking, name='booking'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]