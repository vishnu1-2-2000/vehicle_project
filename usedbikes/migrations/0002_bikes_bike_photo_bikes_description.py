# Generated by Django 4.0.4 on 2022-06-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usedbikes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='bike_photo',
            field=models.ImageField(null=True, upload_to='bikephoto'),
        ),
        migrations.AddField(
            model_name='bikes',
            name='description',
            field=models.CharField(default='exit', max_length=150),
            preserve_default=False,
        ),
    ]
