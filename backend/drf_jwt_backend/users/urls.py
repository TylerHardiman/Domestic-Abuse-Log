from django.urls import path, include
from users import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.get_all_survivors),
    path('all/', views.survivor_survivors),
    path('all/', views.get_abuselog),
    path('all/', views.survivor_abuselog),
]
