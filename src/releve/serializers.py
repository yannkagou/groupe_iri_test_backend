from rest_framework import serializers
from .models import Releve

class ReleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Releve
        fields = '__all__'