# Generated by Django 4.0.5 on 2022-07-15 13:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_created_at_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('b98d33e3-02b7-482d-ad8a-9e0030672098'), editable=False, primary_key=True, serialize=False),
        ),
    ]
