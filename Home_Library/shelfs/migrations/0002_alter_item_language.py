# Generated by Django 3.2.4 on 2021-06-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='language',
            field=models.IntegerField(choices=[(1, 'Polish'), (2, 'English'), (3, 'German'), (4, 'French'), (5, 'Other')]),
        ),
    ]
