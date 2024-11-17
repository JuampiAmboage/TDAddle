from django.urls import path, include
from .views import get_algorithm_of_the_day

urlpatterns = [
    path('', get_algorithm_of_the_day, name='get_algorithm_of_the_day'),
]