# Generated by Django 4.1.1 on 2023-03-21 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_author_description_alter_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverphoto', models.ImageField(upload_to='book/')),
                ('booktitle', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('rating', models.FloatField()),
                ('bookstatus', models.CharField(choices=[('newbook', 'newbook'), ('trending', 'trending'), ('latestbook', 'latestbook'), ('comingsoon', 'comingsoon'), ('available', 'available'), ('out of stock', 'out of stock')], max_length=50)),
                ('authorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]