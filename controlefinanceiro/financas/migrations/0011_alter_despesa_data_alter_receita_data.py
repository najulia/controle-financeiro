# Generated by Django 4.1.5 on 2023-01-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0010_alter_despesa_data_alter_receita_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data',
            field=models.DateField(),
        ),
    ]
