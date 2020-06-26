# Generated by Django 3.0.7 on 2020-06-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('topic', models.CharField(default='workgroup topic', max_length=200)),
                ('supervisor', models.CharField(default='workgroup supervisor', max_length=50)),
                ('number_of_participants', models.IntegerField(default=0)),
            ],
        ),
    ]