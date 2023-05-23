# Generated by Django 4.1.1 on 2023-03-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_category_photo_alter_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
            options={
                'db_table': 'faq',
            },
        ),
    ]
