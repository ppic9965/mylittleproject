# Generated by Django 2.0.1 on 2018-01-21 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0002_auto_20180120_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='webzinedown',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
