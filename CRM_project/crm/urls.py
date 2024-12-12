from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('registration/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('registration/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/signup/', views.signup, name='signup'),
    path('', views.customer_list, name='customer_list'),
    path('add/', views.customer_create, name='customer_create'),
    path('<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('<int:pk>/delete/', views.customer_delete, name='customer_delete'),
]

