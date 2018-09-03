from rest_framework import serializers

from main.models import UsefulNumber, UsefulText


class UsefulNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulNumber
        fields = ('number',)


class UsefulTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulText
        fields = ('text',)
