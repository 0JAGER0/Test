# Generated by Django 3.2.3 on 2021-06-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210609_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='arriendocleta',
            name='marca',
            field=models.CharField(default='', max_length=50, verbose_name='marca bicicleta'),
        ),
    ]
