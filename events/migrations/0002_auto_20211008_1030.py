# Generated by Django 3.2.4 on 2021-10-08 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=12)),
                ('event_location', models.CharField(max_length=10)),
                ('start_time', models.DateTimeField(default=datetime.date.today)),
                ('end_time', models.DateTimeField(default=datetime.date.today)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]