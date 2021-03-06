# Generated by Django 2.2.10 on 2020-02-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soeid', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('status', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=3)),
                ('registered_date', models.DateTimeField()),
            ],
        ),
    ]
