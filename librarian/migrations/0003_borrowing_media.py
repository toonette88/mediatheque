# Generated by Django 5.1 on 2024-09-11 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_alter_media_type_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='media',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='librarian.book'),
        ),
    ]
