from django.urls import path
from sidehustles import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('filtersearch/', views.FilterSearchView.as_view(), name="filtersearch"),
    path('product/', views.ProductView.as_view(), name="product")
]
