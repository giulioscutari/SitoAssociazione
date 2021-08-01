# Generated by Django 3.1.7 on 2021-08-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domande', '0010_remove_domanda_argomento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domanda',
            name='anno',
        ),
        migrations.AddField(
            model_name='domanda',
            name='status',
            field=models.CharField(default='Draft', editable=False, max_length=10),
        ),
    ]
