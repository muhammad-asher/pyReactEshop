from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('', views.getroutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('products/<str:pk>', views.getProduct, name="product"),

]
