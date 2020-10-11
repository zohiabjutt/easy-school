# Generated by Django 3.1.2 on 2020-10-08 18:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
import students.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.IntegerField(unique=True)),
                ('date_of_admission', models.DateField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(default='Not Set', max_length=150)),
                ('is_studying', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, upload_to=students.models.user_directory_path)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_until', models.DateField(default=datetime.date(2020, 11, 1), verbose_name='Valid Until')),
                ('total_amount', models.PositiveIntegerField(default=0)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('social_security_number', models.CharField(max_length=30)),
                ('phone_number', models.CharField(default='0000000', max_length=11)),
                ('profession', models.CharField(default='Not Set', max_length=50)),
                ('relation_to_student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.student')),
            ],
        ),
    ]
