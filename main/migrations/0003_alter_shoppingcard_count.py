# Generated by Django 4.2.5 on 2023-09-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_shoppingcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcard',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
