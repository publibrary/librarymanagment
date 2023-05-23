# Generated by Django 4.1.1 on 2023-03-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='blog/')),
                ('postby', models.CharField(max_length=100)),
                ('poston', models.DateField()),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
