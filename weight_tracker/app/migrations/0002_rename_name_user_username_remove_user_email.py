# Generated by Django 4.2.6 on 2023-10-11 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
