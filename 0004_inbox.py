# Generated by Django 2.1.5 on 2019-02-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0003_auto_20190214_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('userId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
    ]
