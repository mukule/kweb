# Generated by Django 4.1.7 on 2023-03-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='facebook',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='linkedin',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='twitter',
            field=models.CharField(max_length=100),
        ),
    ]