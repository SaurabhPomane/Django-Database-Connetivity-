# Generated by Django 5.1.1 on 2024-10-15 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('mono', models.IntegerField()),
            ],
            options={
                'db_table': 'register_data',
            },
        ),
    ]
