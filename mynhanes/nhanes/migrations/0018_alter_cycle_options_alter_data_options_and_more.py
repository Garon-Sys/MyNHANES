# Generated by Django 5.0.6 on 2024-05-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhanes', '0017_remove_data_nhanes_data_cycle_i_19779b_idx_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cycle',
            options={'ordering': ['cycle'], 'verbose_name_plural': '01-Cycles'},
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name_plural': '07-Data'},
        ),
        migrations.AlterModelOptions(
            name='dataset',
            options={'verbose_name_plural': '03-Dataset'},
        ),
        migrations.AlterModelOptions(
            name='datasetcontrol',
            options={'verbose_name_plural': '06-Donwload Control'},
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name_plural': '04-Field'},
        ),
        migrations.AlterModelOptions(
            name='fieldcycle',
            options={'verbose_name_plural': '05-Field by Cycle'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': '02-Group'},
        ),
        migrations.AlterModelOptions(
            name='querystructure',
            options={'verbose_name_plural': '08-Query Structure'},
        ),
        migrations.AddIndex(
            model_name='fieldcycle',
            index=models.Index(fields=['field', 'cycle'], name='nhanes_fiel_field_i_a7b19e_idx'),
        ),
    ]
