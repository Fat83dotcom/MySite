# Generated by Django 4.2.5 on 2023-09-17 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_category_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
        migrations.AlterField(
            model_name='page',
            name='isPublished',
            field=models.BooleanField(default=False, help_text='Marque para publicar.'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('excerpt', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='posts/%Y/%m/')),
                ('coverInPostContent', models.BooleanField(default=True, help_text='Exibe a imagem no conteudo do post.')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('isPublished', models.BooleanField(default=False, help_text='Marque para publicar.')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.category')),
                ('tag', models.ManyToManyField(blank=True, default='', to='Core.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
