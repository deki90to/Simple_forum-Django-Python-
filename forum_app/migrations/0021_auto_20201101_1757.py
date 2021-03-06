# Generated by Django 3.1.2 on 2020-11-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0020_posts_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]
