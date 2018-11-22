from django.urls import path
from sidehustles import views




urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name="profile"),
    path('filtersearch/', views.filtersearch, name="filtersearch"),
    path('product/<int:pk>', views.product, name="product"),
    path('about/', views.about, name="about"),
    path('change_password/', views.change_password, name="change_password"),
<<<<<<< HEAD
    path('sidehustles/profile_changes/', views.profile_changes, name="profile_changes"),

=======
>>>>>>> 31318742c7185ee3247281caeaf62ad8bd2d7151
    #path('profile/<int:pk>/profile_changes', views.profileChanges, name='profile_changes'),

]
