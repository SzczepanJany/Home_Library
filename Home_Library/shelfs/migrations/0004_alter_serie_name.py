# Generated by Django 3.2.4 on 2021-07-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelfs', '0003_auto_20210708_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
