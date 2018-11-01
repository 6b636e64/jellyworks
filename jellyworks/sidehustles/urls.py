from django.urls import path
from sidehustles import views


urlpatterns = [
    path('', views.index, name='index'),
]
