from django.db import models

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos')
    def __str__(self):
        return self.title

   
        