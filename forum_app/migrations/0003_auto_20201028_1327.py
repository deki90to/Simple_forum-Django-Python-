# Generated by Django 3.1.1 on 2020-10-28 12:27

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0002_auto_20201027_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[480, 320], upload_to='BlogSite/media/'),
        ),
        migrations.AddField(
            model_name='posts',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='BlogSite/media/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(),
        ),
    ]
