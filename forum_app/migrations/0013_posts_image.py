# Generated by Django 3.1.2 on 2020-10-31 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0012_auto_20201031_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
