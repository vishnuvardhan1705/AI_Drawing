from rest_framework import serializers
from .models import drawpage,drawsteps

class drawstepSerializer(serializers.ModelSerializer):
    imageurl=serializers.SerializerMethodField()
    stepnum=serializers.IntegerField(source="stepno")
    step=serializers.CharField(source="steptext")
    class Meta:
        model=drawsteps
        fields=['stepnum','imageurl','step']

    def get_imageurl(self,obj):
        return obj.image.url if obj.image else None

class drawpageSerializer(serializers.ModelSerializer):
    steps=drawstepSerializer(many=True)

    class Meta:
        model=drawpage
        fields=['id','name','description','steps']