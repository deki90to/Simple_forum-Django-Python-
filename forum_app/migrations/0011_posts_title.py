# Generated by Django 3.1.2 on 2020-10-31 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0010_auto_20201031_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]