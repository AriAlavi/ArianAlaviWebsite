from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=128)
    image = models.ImageField(upload_to='projects')

    def __str__(self):
        return f"[{self.name}] {self.description}"