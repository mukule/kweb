# Generated by Django 4.1.7 on 2023-05-04 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_completed_assignment_accepted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField()),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, upload_to='progress_reports/')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_reports', to='tasks.assignment')),
            ],
        ),
    ]
