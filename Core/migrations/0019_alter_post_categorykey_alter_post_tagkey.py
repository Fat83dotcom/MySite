# Generated by Django 4.2.5 on 2023-10-01 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0018_alter_post_categorykey_alter_post_tagkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoryKey',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categoryRel', to='Core.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tagKey',
            field=models.ManyToManyField(blank=True, default='', related_name='tagsRel', to='Core.tag'),
        ),
    ]
