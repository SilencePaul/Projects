# Generated by Django 5.0 on 2023-12-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol_website', '0003_rename_championdetails_championdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='search_name',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
