# Generated by Django 5.1.3 on 2024-11-28 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='name',
            new_name='nombre',
        ),
    ]
