from django.db import models

# Create your models here.
class Job (models.Model):
    title = models.CharField(default= 'Project', max_length = 50)
    image = models.ImageField(upload_to = 'images/')
    summary = models.TextField(max_length = 200)

    def __str__(self):
        return  self.title
