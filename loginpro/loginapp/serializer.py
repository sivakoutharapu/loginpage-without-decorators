from rest_framework import serializers
from .models import modellogin

class loginserializers(serializers.ModelSerializer):
    class Meta():
        model = modellogin
        fields = '__all__'
        
        
        
        
        