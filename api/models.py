from django.db import models

class drawpage(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.Name
    
class drawsteps(models.Model):
    stepcontent=models.ForeignKey(drawpage,related_name="stepdiscription",on_delete=models.CASCADE)
    stepno=models.IntegerField()
    image=models.ImageField(upload_to="image/")
    steptext=models.CharField(300)

    def __str__(self):
        return f"Step {self.stepno} for {self.stepcontent.name}"