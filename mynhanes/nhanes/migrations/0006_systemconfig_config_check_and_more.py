# Generated by Django 5.0.8 on 2024-08-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nhanes", "0005_alter_workprocess_last_synced_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="systemconfig",
            name="config_check",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="systemconfig",
            name="config_value",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
