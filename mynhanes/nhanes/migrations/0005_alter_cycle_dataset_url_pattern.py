# Generated by Django 5.0.6 on 2024-05-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhanes', '0004_alter_datasetcontrol_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycle',
            name='dataset_url_pattern',
            field=models.CharField(default='%s/%s/', max_length=255),
        ),
    ]
