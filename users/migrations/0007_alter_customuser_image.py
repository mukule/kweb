# Generated by Django 4.1.7 on 2023-03-24 08:05

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default/user.png', upload_to=users.models.CustomUser.image_upload_to),
        ),
    ]