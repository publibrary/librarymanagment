# Generated by Django 4.1.1 on 2023-03-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='author/')),
                ('name', models.CharField(max_length=100)),
                ('name1', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]