# Generated by Django 2.2.7 on 2019-12-07 20:54

from django.db import migrations, models
import storage


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(storage=storage.MyStorage(), upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='out_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
