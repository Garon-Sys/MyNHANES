# Generated by Django 5.0.6 on 2024-05-29 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhanes', '0019_alter_queryfilter_filter_name'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='data',
            name='nhanes_data_cycle_i_4b523f_idx',
        ),
        migrations.AlterUniqueTogether(
            name='data',
            unique_together=set(),
        ),
    ]