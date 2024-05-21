# Generated by Django 4.1.5 on 2023-04-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
