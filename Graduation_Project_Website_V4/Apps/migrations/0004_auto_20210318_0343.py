# Generated by Django 3.0.5 on 2021-03-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0003_auto_20210318_0325'),
    ]

    operations = [
        migrations.DeleteModel(
            name='quiz_results',
        ),
        migrations.AlterField(
            model_name='applicantcv',
            name='pdf_cv',
            field=models.FileField(max_length=50, upload_to=''),
        ),
    ]
