# Generated by Django 5.0.6 on 2024-06-04 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='other_details',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]