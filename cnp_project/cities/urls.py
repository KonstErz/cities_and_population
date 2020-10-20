from django.urls import path
from cities import views


urlpatterns = [
    path('cities/', views.city_list, name='cities'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.log_out, name='logout')
]
