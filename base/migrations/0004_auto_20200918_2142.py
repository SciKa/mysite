# Generated by Django 3.1.1 on 2020-09-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200918_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpstime',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gpstime',
            name='lat',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='gpstime',
            name='long',
            field=models.CharField(max_length=200),
        ),
    ]
