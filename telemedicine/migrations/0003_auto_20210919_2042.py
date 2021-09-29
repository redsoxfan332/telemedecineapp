# Generated by Django 3.2.7 on 2021-09-20 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0002_patients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='familyhistory',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='patients',
            name='smoking',
            field=models.BooleanField(default=False),
        ),
    ]
