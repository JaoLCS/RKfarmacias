from django.db import models

# Create your models here.

class remedios(models.Model):
    EMB_CHOICES= [
        [1, "Envelope"],
        [2, "Bisnaga"],
        [3, "Bolsa"],
        [4, "Ampolas"],
        [5, "Seringa"],
        [6, "Frasco"],
        [7, "Blísteres"]
    ]
    rem_remedio = models.CharField(max_length = 45)
    rem_preco = models.FloatField()
    rem_quantidade = models.IntegerField()
    rem_embalagem = models.IntegerField(choices= EMB_CHOICES)
    def __str__(self):
        return (self.rem_remedio)
    class Meta:
        verbose_name_plural = "Remédios"