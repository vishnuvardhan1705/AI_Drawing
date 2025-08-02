from django.db import models

class drawpage(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

   
    
class drawsteps(models.Model):
    stepcontent=models.ForeignKey(drawpage,related_name="stepdiscription",on_delete=models.CASCADE)
    stepno=models.IntegerField()
    image=models.ImageField()
    steptext=models.CharField(300)
