from django.db import models
from .choices import ChoicesCategoriaRelatorio
from datetime import datetime
from secrets import token_hex
import secrets


# Create your models here.
class CategoriaRelatorio (models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaRelatorio.choices)
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.titulo


class Relatorio(models.Model):
    titulo = models.CharField(max_length=50)
    categoria_relatorio = models.ManyToManyField(CategoriaRelatorio)
    data_geracao = models.DateField(null=True)
    protocolo = models.CharField(max_length=52, null=True, blank=True)
    identificador = models.CharField(max_length=24, null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime("%d/%m/%Y-%H:%M:%S-") + token_hex(16)

        if not self.identificador:
            self.identificador = secrets.token_urlsafe(16)  # noqa: F821

        super(Relatorio, self).save(*args, **kwargs)

    def valor_total(self):
        valor_total = float(0)
        for categoria in self.categoria_relatorio.all():
            valor_total += float(categoria.valor)
        return valor_total
