# Generated by Django 2.1.7 on 2019-04-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_pjts_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='pjts_coins',
            field=models.DecimalField(decimal_places=8, max_digits=28),
        ),
    ]
