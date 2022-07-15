# Generated by Django 4.0.5 on 2022-07-15 14:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('63a1f794-551b-48a6-8b7a-ea5a2b6153af'), editable=False, primary_key=True, serialize=False),
        ),
    ]
