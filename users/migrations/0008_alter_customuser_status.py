# Generated by Django 4.1.7 on 2023-04-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('Attachment', 'Attachment'), ('Intern', 'Intern'), ('Contract', 'Contract'), ('Permanent', 'Permanent')], default='regular', max_length=100),
        ),
    ]
