# Generated by Django 4.0.5 on 2022-06-26 12:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.UUID('06822909-7d3a-4129-9382-cc7f292e9e62'), editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('todo_title', models.CharField(max_length=100)),
                ('todo_description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
