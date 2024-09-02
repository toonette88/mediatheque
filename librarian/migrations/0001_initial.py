# Generated by Django 5.1 on 2024-09-02 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('creator', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('availability', models.BooleanField(default='')),
                ('borrower', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='librarian.media')),
                ('author', models.CharField(max_length=150)),
            ],
            bases=('librarian.media',),
        ),
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='librarian.media')),
                ('entertainer', models.CharField(max_length=150)),
            ],
            bases=('librarian.media',),
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='librarian.media')),
                ('producer', models.CharField(max_length=150)),
            ],
            bases=('librarian.media',),
        ),
    ]
