# Generated by Django 3.1.1 on 2020-09-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200920_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
