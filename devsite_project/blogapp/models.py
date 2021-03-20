from django.db import models

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date',]
   
        