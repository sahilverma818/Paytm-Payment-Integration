from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', views.payment, name='payment'),
    path('handlerequest/', views.handlerequest, name='handlerequest'),
]