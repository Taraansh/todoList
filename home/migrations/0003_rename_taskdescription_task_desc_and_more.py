# Generated by Django 4.1.7 on 2023-03-02 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_tasks_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='taskDescription',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='taskTitle',
            new_name='title',
        ),
    ]