from django.db.models import TextChoices


class ChoicesCategoriaRelatorio(TextChoices):
    TERMO_COMPROMISSO_AMBIENTAL = ("TCA", "Termo de Compromisso Ambiental")
    AUTORIZACAO_AMBIENTAL = ("AA", "Autorização Ambiental")
