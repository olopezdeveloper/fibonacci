
from rest_framework import serializers

from api.models import Fibonacci


class FibonacciSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fibonacci
        fields = ('value', 'fibonacci_number')
        read_only_fields = ('fibonacci_number',)

    def create(self, validated_data):
        value = validated_data['value']
        fibonacci_number = Fibonacci.caculate_fibonacci_number(value)


        return Fibonacci.objects.create(
            value=value,
            fibonacci_number = fibonacci_number
        )
