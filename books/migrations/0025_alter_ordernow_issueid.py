# Generated by Django 4.1.1 on 2023-05-18 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_remove_ordernow_userid_ordernow_issueid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordernow',
            name='issueid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='books.issuebook'),
        ),
    ]
