# Generated by Django 4.2.2 on 2023-07-13 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 15, 23, 45, 281811, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 15, 23, 45, 281373, tzinfo=datetime.timezone.utc)),
        ),
    ]
