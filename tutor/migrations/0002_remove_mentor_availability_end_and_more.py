# Generated by Django 5.1.4 on 2024-12-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='availability_end',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='availability_start',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='engagement_score',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='teaching_style',
        ),
        migrations.AddField(
            model_name='mentor',
            name='available_time',
            field=models.CharField(default='Not Available', max_length=255),
        ),
        migrations.AddField(
            model_name='mentor',
            name='expertise',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='mentor',
            name='teaching_mode',
            field=models.CharField(default='virtual', max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
