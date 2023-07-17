
from django.urls import path
from bankapp import views

app_name = 'bankapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('page/', views.page, name='page'),
    path('form/', views.form, name='form'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('success/', views.success_page, name='success_page'),
    path('redirect/<str:district>/', views.redirect_to_wikipedia, name='redirect_to_wikipedia'),
]

