# Generated by Django 3.1.7 on 2021-05-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0021_auto_20190118_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
