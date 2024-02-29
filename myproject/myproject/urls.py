from django.contrib import admin
from django.urls import path
from myapp.views import phone_create, phone_delete, phone_detail, phone_list, phone_update
urlpatterns = [
     path('admin/', admin.site.urls) ,
      path('', phone_list, name='phone_list'),
    path('phone/<int:pk>/', phone_detail, name='phone_detail'),
    path('phone/new/', phone_create, name='phone_create'),
    path('phone/<int:pk>/edit/', phone_update, name='phone_update'),
    path('phone/<int:pk>/delete/', phone_delete, name='phone_delete'),
]

