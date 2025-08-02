from rest_framework import serializers
from .models import drawpage,drawsteps

class drawstepsSerializer(serializers.ModelSerializer):
    class Meta:
        model=drawsteps
        fields=['stepno','image','steptext']

class drawpageSerializer(serializers.ModelSerializer):
    stepdiscription=drawstepsSerializer(many=True)
    class Meta:
        model=drawpage
        fields=['id','name','description','stepdiscription']