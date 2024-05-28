# Generated by Django 5.0.6 on 2024-05-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhanes', '0006_alter_cycle_dataset_url_pattern_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='dataset',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='internal_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]