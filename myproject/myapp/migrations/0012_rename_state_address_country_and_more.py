# Generated by Django 5.0.1 on 2024-02-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_kifle_ketema_address_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='state',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='address_line1',
        ),
        migrations.RemoveField(
            model_name='address',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='address',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
    ]