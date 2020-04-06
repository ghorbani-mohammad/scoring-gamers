from django.urls import path
from gamers import views

urlpatterns = [
    path('gamers/', views.gamer_list),
    path('gamers/<str:mobile>/', views.gamer_detail),
]