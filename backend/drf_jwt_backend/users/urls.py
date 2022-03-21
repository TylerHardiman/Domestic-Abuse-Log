from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.user_users),
    path('all/', views.get_all_users),
    path('', views.user_abuselog),
    path('all', views.get_all_abuselog),

]