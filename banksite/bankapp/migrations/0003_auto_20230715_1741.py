# Generated by Django 3.2.20 on 2023-07-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_remove_form_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='materials_provided',
            new_name='materials_provide',
        ),
        migrations.AddField(
            model_name='form',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
