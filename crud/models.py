from django.db import models

# Create your models here.

class remedios(models.Model):
    EMB_CHOICES= [
        ["Envelope", "Envelope"],
        ["Bisnaga", "Bisnaga"],
        ["Bolsa", "Bolsa"],
        ["Ampolas", "Ampolas"],
        ["Seringa", "Seringa"],
        ["Frasco", "Frasco"],
        ["Blísteres", "Blísteres"]
    ]
    rem_remedio = models.CharField(max_length = 45)
    rem_preco = models.FloatField()
    rem_quantidade = models.IntegerField()
    rem_embalagem = models.CharField(max_length= 20 ,choices= EMB_CHOICES)
    def __str__(self):
        return (self.rem_remedio)
    class Meta:
        verbose_name_plural = "Remédios"