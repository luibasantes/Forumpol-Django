# Generated by Django 2.0 on 2018-01-01 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foro', '0002_auto_20171231_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posted_images'),
        ),
    ]