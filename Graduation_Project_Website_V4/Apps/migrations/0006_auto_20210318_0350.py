# Generated by Django 3.0.5 on 2021-03-18 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0005_auto_20210318_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantcv',
            name='pdf_cv',
            field=models.CharField(max_length=50),
        ),
    ]
