# Generated by Django 5.1.1 on 2024-10-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Emp_name', models.CharField(max_length=20)),
                ('Emp_salary', models.BigIntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
