from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FibonacciViewSet


router = DefaultRouter()
router.register(r'fibonacci', FibonacciViewSet, basename='fibonacci')
urlpatterns = [

	path('', include(router.urls)),

]
