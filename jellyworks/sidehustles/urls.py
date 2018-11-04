from django.urls import path
from sidehustles import views




urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name="profile"),
    path('filtersearch/', views.filtersearch, name="filtersearch"),
    path('product/', views.ProductView.as_view(), name="product"),
    path('about/', views.about, name="about")

]
