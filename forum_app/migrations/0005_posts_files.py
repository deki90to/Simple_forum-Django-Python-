# Generated by Django 3.1.2 on 2020-10-30 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0004_auto_20201029_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='files',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
