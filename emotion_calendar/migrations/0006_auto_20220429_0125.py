# Generated by Django 3.1.14 on 2022-04-29 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_calendar', '0005_alter_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
