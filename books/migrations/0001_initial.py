# Generated by Django 4.1.1 on 2023-02-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('Mobileno', models.IntegerField()),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
