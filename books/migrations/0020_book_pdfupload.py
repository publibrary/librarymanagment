# Generated by Django 4.1.1 on 2023-04-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_alter_book_booktitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdfupload',
            field=models.FileField(default='', upload_to='pdfs/'),
        ),
    ]