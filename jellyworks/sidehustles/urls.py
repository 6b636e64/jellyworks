from django.urls import path
from sidehustles import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name="profile"),
    path('filtersearch/', views.filtersearch, name="filtersearch"),
    path('product/<int:pk>', views.product, name="product"),
    path('about/', views.about, name="about"),
    path('change_password/', views.change_password, name="change_password"),
    path('sidehustles/profile_changes/', views.profile_changes, name="profile_changes"),

    #path('profile/<int:pk>/profile_changes', views.profileChanges, name='profile_changes'),

]
