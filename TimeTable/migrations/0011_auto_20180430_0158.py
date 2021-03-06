# Generated by Django 2.0.4 on 2018-04-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0010_auto_20180430_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.CharField(choices=[(1, 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'Jule'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='month',
            name='week_days',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
