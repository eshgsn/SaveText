# Generated by Django 4.0.5 on 2024-02-07 17:08

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataId', models.UUIDField(default=uuid.UUID('a65890dc-33c9-45cc-9877-671e3a2e0f63'), unique=True)),
                ('fileName', models.CharField(max_length=30)),
                ('textFile', models.TextField(blank=True, null=True)),
                ('ownerUserId', models.UUIDField()),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2024, 2, 7, 22, 38, 8, 276186))),
                ('updatedAt', models.DateTimeField(default=datetime.datetime(2024, 2, 7, 22, 38, 8, 276186))),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 22, 38, 8, 276186)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 22, 38, 8, 276186)),
        ),
        migrations.AlterField(
            model_name='users',
            name='userId',
            field=models.UUIDField(default=uuid.UUID('9e664a45-a8dc-457f-87f6-f7e6741b52cb'), unique=True),
        ),
    ]
