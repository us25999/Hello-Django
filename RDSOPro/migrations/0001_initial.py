# Generated by Django 4.0.6 on 2022-07-17 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('role_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='RDSOPro.roles')),
            ],
        ),
        migrations.CreateModel(
            name='DrawerFields',
            fields=[
                ('field_id', models.IntegerField(primary_key=True, serialize=False)),
                ('field', models.CharField(max_length=100)),
                ('field_link', models.URLField()),
                ('role_id', models.ManyToManyField(blank=True, related_name='drawerField', to='RDSOPro.roles')),
            ],
        ),
    ]
