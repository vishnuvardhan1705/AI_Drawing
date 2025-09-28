from django.db import models

class drawpage(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(max_length=100,null=True)

   
    
class drawsteps(models.Model):
    stepcontent=models.ForeignKey(drawpage,related_name="stepdiscription",on_delete=models.CASCADE)
    stepno=models.IntegerField()
    image=models.ImageField(upload_to="", blank=True, null=True)
    steptext=models.CharField(300)
