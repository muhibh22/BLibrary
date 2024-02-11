from django.db import models

# Create your models here.


class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    author=models.CharField(max_length=50)

    def __str__(self):
        return self.title