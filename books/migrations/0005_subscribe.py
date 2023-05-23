# Generated by Django 4.1.1 on 2023-03-10 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=100)),
                ('current_datetime', models.DateField(default=datetime.date(2023, 3, 10))),
            ],
            options={
                'db_table': 'subscribe',
            },
        ),
    ]