# Generated by Django 4.1.7 on 2023-03-24 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='description',
            new_name='mood',
        ),
    ]