# Generated by Django 4.1.4 on 2022-12-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
