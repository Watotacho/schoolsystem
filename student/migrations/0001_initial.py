# Generated by Django 3.2.4 on 2021-08-14 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=10)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('date_of_birth', models.DateField()),
                ('guardian_name', models.CharField(max_length=12)),
                ('guardian_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('guardian_phone_number', models.CharField(max_length=12)),
                ('class_name', models.CharField(max_length=12)),
                ('room_number', models.CharField(max_length=12)),
                ('laptop_number', models.PositiveSmallIntegerField(max_length=30, null=True)),
                ('health_records', models.FileField(upload_to='')),
                ('academic_year', models.IntegerField(default=0)),
            ],
        ),
    ]
