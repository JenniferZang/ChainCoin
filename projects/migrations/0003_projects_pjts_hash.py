# Generated by Django 2.1.7 on 2019-04-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_pjts_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='pjts_hash',
            field=models.CharField(default='false', max_length=400),
        ),
    ]
