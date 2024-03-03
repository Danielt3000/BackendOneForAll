from django.db import models

# Create your models here.


class Gatos(models.Model):
    tipo_de_gato = models.CharField(max_length=250)

    def __str__(self):
        return self.title