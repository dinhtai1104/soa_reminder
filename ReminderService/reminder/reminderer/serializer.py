from rest_framework import serializers

from reminderer.models import Car

class CarSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Car
        fields = 'name', 'color', 'brand'