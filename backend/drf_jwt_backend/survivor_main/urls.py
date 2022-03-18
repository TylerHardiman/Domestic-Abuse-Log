from django.urls import path, include
from .import views
# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.get_all_survivors),
    path('all/', views.Survivor_victim),
    path('all/', views.get_abuselog),
]