# Generated by Django 5.0.6 on 2024-05-29 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhanes', '0016_data_sequence'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='data',
            name='nhanes_data_cycle_i_19779b_idx',
        ),
        migrations.AlterUniqueTogether(
            name='data',
            unique_together={('cycle', 'dataset', 'field', 'sample', 'sequence')},
        ),
        migrations.AddIndex(
            model_name='data',
            index=models.Index(fields=['cycle', 'dataset', 'field', 'sample', 'sequence'], name='nhanes_data_cycle_i_4b523f_idx'),
        ),
    ]
