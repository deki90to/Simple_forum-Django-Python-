# Generated by Django 3.1.1 on 2020-10-28 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0003_auto_20201028_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='video',
        ),
    ]