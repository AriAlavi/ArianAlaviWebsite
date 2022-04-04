# Generated by Django 4.0.3 on 2022-04-04 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_project_skillsused'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='percent_ability',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
