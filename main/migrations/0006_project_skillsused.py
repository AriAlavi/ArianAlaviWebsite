# Generated by Django 4.0.3 on 2022-04-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skillsUsed',
            field=models.ManyToManyField(to='main.skill'),
        ),
    ]
