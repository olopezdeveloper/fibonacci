from django.db import models

# Create your models here.


class Fibonacci(models.Model):

    value = models.BigIntegerField()
    fibonacci_number = models.BigIntegerField()

    @staticmethod
    def caculate_fibonacci_number(value):
        
        if value <= 1:
            return value
        
        return Fibonacci.caculate_fibonacci_number(value-1) + Fibonacci.caculate_fibonacci_number(value-2)
