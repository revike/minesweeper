# Generated by Django 5.0.2 on 2024-02-15 16:24

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='game_id')),
                ('width', models.IntegerField(default=10, verbose_name='width')),
                ('height', models.IntegerField(default=10, verbose_name='height')),
                ('mines_count', models.IntegerField(default=5, verbose_name='mines_count')),
                ('completed', models.BooleanField(default=False, verbose_name='completed')),
            ],
            options={
                'verbose_name': 'game',
                'verbose_name_plural': 'games',
            },
        ),
        migrations.CreateModel(
            name='GameField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.JSONField(verbose_name='field')),
                ('field_bomb', models.JSONField(verbose_name='bomb field')),
                ('game_field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='main.game', verbose_name='game')),
            ],
            options={
                'verbose_name': 'game field',
                'verbose_name_plural': 'game fields',
            },
        ),
    ]
