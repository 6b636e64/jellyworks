from django.urls import path
from sidehustles import views




urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name="profile"),
    path('filtersearch/', views.filtersearch, name="filtersearch"),
    path('product/<int:pk>', views.product, name="product"),
    path('about/', views.about, name="about"),
    #path('password_reset_confirm/', views.password_reset_confirm, name="password_reset_confirm"),

]
