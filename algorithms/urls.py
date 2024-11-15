from django.urls import path, include
from rest_framework import routers
from algorithms import views

router = routers.DefaultRouter()
router.register(r'algorithms', views.AlgorithmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]