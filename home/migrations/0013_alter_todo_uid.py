# Generated by Django 4.0.5 on 2022-07-15 15:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('82ecaf8b-139b-4709-beeb-d58f61033e2c'), editable=False, primary_key=True, serialize=False),
        ),
    ]