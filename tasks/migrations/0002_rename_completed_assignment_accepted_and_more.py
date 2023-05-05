# Generated by Django 4.1.7 on 2023-05-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='completed',
            new_name='accepted',
        ),
        migrations.AddField(
            model_name='assignment',
            name='rejection_reason',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('I', 'In Progress'), ('C', 'Complete')], default='P', max_length=1),
        ),
    ]
