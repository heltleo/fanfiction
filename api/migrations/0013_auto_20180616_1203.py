# Generated by Django 2.0.2 on 2018-06-16 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_auto_20180318_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowStories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fanfic', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ml_content', models.TextField()),
                ('cgu_content', models.TextField()),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
        ),
        migrations.RemoveField(
            model_name='fanfic',
            name='likes',
        ),
        migrations.AddField(
            model_name='fanfic',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='fanfics_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fanfic',
            name='status',
            field=models.CharField(choices=[('brouillon', 'Brouillon'), ('publié', 'Publié')], default='brouillon', max_length=10),
        ),
        migrations.AddField(
            model_name='followstories',
            name='to_fanfic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.Fanfic'),
        ),
    ]
