# Generated by Django 4.2.5 on 2024-04-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetup', '0011_sitesetuppicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='index_description_3_1',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='index_description_3_2',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
