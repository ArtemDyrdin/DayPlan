# Generated by Django 3.1.4 on 2021-03-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyplan', '0014_auto_20210328_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='theme',
            field=models.BooleanField(default=True, verbose_name='theme'),
        ),
    ]
