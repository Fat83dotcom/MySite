# Generated by Django 4.2.5 on 2023-09-24 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_remove_portfolioprojects_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioprojects',
            old_name='descritptionCard',
            new_name='descriptionCard',
        ),
    ]
