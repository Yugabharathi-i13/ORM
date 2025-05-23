# Generated by Django 5.2.1 on 2025-05-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=50)),
                ('release_year', models.IntegerField()),
                ('director', models.CharField()),
                ('genre', models.CharField()),
                ('average_rating', models.FloatField()),
            ],
        ),
    ]
