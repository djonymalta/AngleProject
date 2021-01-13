from django.urls import path
from . import views


urlpatterns = [
    path('clock/<int:hours>/<int:minuts>/', views.calculate_angle),
    # path('clock/<int:hours>', views.calculate_angle),
]
