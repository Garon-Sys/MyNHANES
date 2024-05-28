# Generated by Django 5.0.6 on 2024-05-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhanes', '0009_querycolumns_querystructure_queryfilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='querycolumns',
            name='internal_data_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='querycolumns',
            name='column_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]