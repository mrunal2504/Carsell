# Generated by Django 3.0.7 on 2021-03-07 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200625_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='google_plus_link',
            new_name='google_link',
        ),
    ]
