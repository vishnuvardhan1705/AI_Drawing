from django.db import models

class apple(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()

    def __str__(self):
        return self.Name
    
class drawsteps(models.Model):
    step=models.IntegerField()
    image=models.ImageField(upload_to="images")
    steps=models.TextField()
