from django.shortcuts import render
from api.models import Fibonacci
from api.serializer import FibonacciSerializer
# Create your views here.

from rest_framework.viewsets import ModelViewSet






class FibonacciViewSet(ModelViewSet):
    serializer_class = FibonacciSerializer
    queryset = Fibonacci.objects.all()
