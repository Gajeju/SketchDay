

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('artist', models.CharField(max_length=256)),
                ('lyric', models.TextField()),
                ('genre', models.CharField(max_length=64)),
                ('release_date', models.CharField(max_length=32)),
                ('vector', models.TextField()),
                ('sentiment', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=256)),
                ('rate', models.FloatField(default=0)),
                ('rate_cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('dt_created', models.DateField()),
                ('public_TF', models.BooleanField(choices=[(True, '공개'), (False, '비공개')], default=True)),
                ('comment_TF', models.BooleanField(choices=[(True, '허용'), (False, '비허용')], default=True)),
                ('image', models.ImageField(blank=True, upload_to='diary_img/')),
                ('emotion', models.CharField(max_length=20)),
                ('vector', models.CharField(max_length=65535)),
                ('music_no', models.IntegerField()),
                ('emotion_value', models.TextField()),
                ('rate', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
