# Generated by Django 5.0.4 on 2025-02-24 07:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('num_emp', models.IntegerField()),
                ('dean', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('num_teachers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('head_of_department', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.college')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ssn', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.CharField(max_length=255)),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
