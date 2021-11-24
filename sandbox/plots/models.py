from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class Csv(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.FileField(upload_to='plots')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
