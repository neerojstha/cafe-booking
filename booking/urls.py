from . import views

from django.urls import path

#app_name = 'booking'  # Add this line to set the app name for namespacing

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_booking', views.create_booking, name='create_booking'),
    path('list/', views.booking_list, name='booking_list'),
    path('<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]