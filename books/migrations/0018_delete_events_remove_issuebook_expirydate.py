# Generated by Django 4.1.1 on 2023-04-15 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_issuebook'),
    ]

    operations = [
        migrations.DeleteModel(
            name='events',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='expirydate',
        ),
    ]
