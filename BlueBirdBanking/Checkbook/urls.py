from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.home, name="index"),
    path('create/', views.create_account, name="create"),
    path('<int:pk>/balance/', views.balance, name="balance"),
    path('transaction/', views.transaction, name="transaction"),


]