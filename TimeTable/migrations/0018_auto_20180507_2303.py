# Generated by Django 2.0.4 on 2018-05-07 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0017_auto_20180507_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mechanic',
            options={'permissions': (('can_add_mod_mechanic', 'Create and modify mechanic'),)},
        ),
        migrations.AlterModelOptions(
            name='month',
            options={'permissions': (('can_add_month', 'Create a month'),)},
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'permissions': (('can_add_mod_timetable', 'Create and modify timetable'),)},
        ),
    ]
