# Generated by Django 4.0.5 on 2022-07-15 15:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('3781dff8-39d6-4aff-8167-16aee1ef080e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
