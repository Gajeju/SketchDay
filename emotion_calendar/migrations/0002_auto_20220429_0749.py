# Generated by Django 3.1.14 on 2022-04-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]