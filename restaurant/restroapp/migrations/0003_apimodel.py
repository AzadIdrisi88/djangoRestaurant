# Generated by Django 4.2.2 on 2023-09-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroapp', '0002_bookmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='apimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('jsondata', models.CharField(max_length=1000)),
            ],
        ),
    ]