# Generated by Django 4.0.3 on 2022-03-31 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_project_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-endDate']},
        ),
        migrations.AddField(
            model_name='project',
            name='endDate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='startDate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=128),
        ),
    ]
