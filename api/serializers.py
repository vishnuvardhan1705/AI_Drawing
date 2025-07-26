from rest_framework import serializers
from .models import drawpage,drawsteps

class drawstepsSerializer(serializers.ModelSerializer):
    stepnum=serializers.IntegerField(source='stepno')
    imageurl=serializers.CharField(source='image')
    class Meta:
        model=drawsteps
        fields=['stepnum','imageurl','steptext']

class drawpageSerializer(serializers.ModelSerializer):
    stepdiscription=drawstepsSerializer(many=True)
    class Meta:
        model=drawpage
        fields=['id','name','description','stepdiscription']