# Generated by Django 3.0.7 on 2020-07-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='img_url',
            field=models.URLField(default='http://www.lavozdecataratas.com/contenido/fotos/05062020_073730.jpg'),
        ),
    ]
