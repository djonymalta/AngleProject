from django.urls import path
from . import views


urlpatterns = [
    path('clock/<int:hours>/<int:minuts>/', views.calc_angle),
]
