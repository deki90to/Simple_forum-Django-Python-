# Generated by Django 3.1.1 on 2020-10-27 22:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]