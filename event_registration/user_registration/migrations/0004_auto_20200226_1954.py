# Generated by Django 2.2.10 on 2020-02-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0003_auto_20200226_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('registration_cap', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='role',
            old_name='shortName',
            new_name='short_name',
        ),
    ]