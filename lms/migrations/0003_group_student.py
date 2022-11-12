# Generated by Django 4.1.3 on 2022-11-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fancy_number', models.CharField(max_length=20)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='lms.direction')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='lms.group')),
            ],
        ),
    ]