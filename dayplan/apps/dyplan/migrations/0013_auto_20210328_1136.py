# Generated by Django 3.1.4 on 2021-03-28 09:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dyplan', '0012_auto_20210327_2148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnotherUserFields',
            new_name='Profile',
        ),
    ]
