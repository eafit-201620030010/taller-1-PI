from django.db import models
import uuid

class Measure(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     type = models.CharField(verbose_name='Tipo', max_length=20)
     value = models.IntegerField(verbose_name='Valor')
     codigo = models.IntegerField(verbose_name='Codigo')
     longitud = models.FloatField(verbose_name='longitud')
     latitud = models.FloatField(verbose_name='latitud')
     terreno = models.CharField(verbose_name='terreno', max_length=20)
     area = models.PositiveIntegerField(verbose_name='area')
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)


     #codigo = models.IntegerField(verbose_name='Codigo')

