# Generated by Django 4.0.6 on 2022-09-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=40)),
                ('assigned_by', models.CharField(max_length=20)),
            ],
        ),
    ]
