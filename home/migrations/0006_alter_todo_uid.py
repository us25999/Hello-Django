# Generated by Django 4.0.5 on 2022-07-13 10:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('562132d1-f082-4b74-8520-60e890678031'), editable=False, primary_key=True, serialize=False),
        ),
    ]
