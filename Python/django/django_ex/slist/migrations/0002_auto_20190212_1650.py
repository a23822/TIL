# Generated by Django 2.1.7 on 2019-02-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(verbose_name='%m/%d'),
        ),
    ]
