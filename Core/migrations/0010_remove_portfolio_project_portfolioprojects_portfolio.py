# Generated by Django 4.2.5 on 2023-09-23 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_rename_tite_portfolio_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='project',
        ),
        migrations.AddField(
            model_name='portfolioprojects',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.portfolio'),
        ),
    ]
