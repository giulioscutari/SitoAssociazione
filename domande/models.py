from django.db import models

# Create your models here.

gp = (
    ('Canale A', 'CANALE A'),
    ('Canale B', 'CANALE B'),
    ('Canale C', 'CANALE C'),
    ('Canale D', 'CANALE D'),
    ('Canale HT', 'CANALE HT'),
)

an = (
    ('I', 'Primo'),
    ('II', 'Secondo'),
    ('III', 'Terzo'),
    ('IV', 'Quarto'),
    ('V', 'Quinto'),
    ('VI', 'Sesto'),
)

class Materia(models.Model):
    materia = models.CharField(max_length=250, help_text='Inserire il titolo della materia')

    def __str__(self) -> str:
        return self.materia

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materie'

class Domanda(models.Model):
    id = models.IntegerField(editable=False, unique=True, primary_key=True)
    domanda = models.TextField(help_text='Le domande fatte', default='')
    prof = models.TextField(help_text='Il professore che ti ha interrogato', default='')
    gruppo = models.CharField(max_length=10, choices=gp, default=gp[0][0])
    anno = models.CharField(max_length=3, choices=an, default=an[0][0])
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    punteggio = models.IntegerField(help_text='Quante volte è stata ripetuta questa domanda', default=1)
    username = models.TextField(default='')

    class Meta:
        verbose_name = 'Domanda'
        verbose_name_plural = 'Domande'


