# Generated by Django 4.1.5 on 2023-01-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0005_despesa_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('A', 'alimentacao'), ('S', 'saude'), ('M', 'moradia'), ('T', 'transporte'), ('E', 'educacao'), ('L', 'lazer'), ('I', 'imprevistos'), ('O', 'outras')], default='O', max_length=1),
        ),
    ]