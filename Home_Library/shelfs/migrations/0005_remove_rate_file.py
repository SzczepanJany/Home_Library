# Generated by Django 3.2.4 on 2021-07-01 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelfs', '0004_auto_20210630_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='file',
        ),
    ]