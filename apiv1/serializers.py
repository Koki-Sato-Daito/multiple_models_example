from rest_framework import serializers

from app1.models import App1
from app2.models import App2


class App1Serializer(serializers.ModelSerializer):
    class Meta:
        model = App1
        fields = '__all__'

   
class App2Serializer(serializers.ModelSerializer):
    class Meta:
        model = App2
        fields = '__all__'
