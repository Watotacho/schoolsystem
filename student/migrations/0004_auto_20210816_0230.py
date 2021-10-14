# Generated by Django 3.2.4 on 2021-08-16 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_laptop_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.CharField(default=20, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=30, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_phone_number',
            field=models.CharField(default=30, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=20, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=30, max_length=12, null=True),
        ),
    ]