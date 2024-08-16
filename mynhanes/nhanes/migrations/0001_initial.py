# Generated by Django 5.0.8 on 2024-08-09 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cycle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cycle", models.CharField(max_length=100, unique=True)),
                ("base_dir", models.CharField(default="downloads", max_length=255)),
                ("year_code", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "base_url",
                    models.URLField(default="https://wwwn.cdc.gov/Nchs/Nhanes"),
                ),
                (
                    "dataset_url_pattern",
                    models.CharField(default="%s/%s/%s", max_length=255),
                ),
            ],
            options={
                "verbose_name_plural": "01-Cycles",
                "ordering": ["cycle"],
            },
        ),
        migrations.CreateModel(
            name="Dataset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dataset", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "03-Dataset",
            },
        ),
        migrations.CreateModel(
            name="Field",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "field_type",
                    models.CharField(
                        choices=[
                            ("bin", "Binary"),
                            ("cat", "Category"),
                            ("num", "Numeric"),
                            ("tex", "Text"),
                            ("oth", "Other"),
                        ],
                        default="oth",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "Field",
                "verbose_name_plural": "Field",
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("group", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "02-Group",
            },
        ),
        migrations.CreateModel(
            name="QueryColumns",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("column_name", models.CharField(max_length=100, unique=True)),
                (
                    "internal_data_key",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("column_description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="SystemConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("config_key", models.CharField(max_length=100, unique=True)),
                ("config_value", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=50, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Variable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("variable", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "04-Variable",
            },
        ),
        migrations.CreateModel(
            name="WorkProcessMasterData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "component_type",
                    models.CharField(
                        choices=[
                            ("rule", "Normalizations Rule"),
                            ("cycle", "Cycle"),
                            ("dataset", "Dataset"),
                            ("variable", "Variable"),
                            ("variable_cycle", "VariableCycle"),
                        ],
                        max_length=20,
                    ),
                ),
                ("last_synced_at", models.DateTimeField(auto_now_add=True)),
                (
                    "source_file_version",
                    models.CharField(blank=True, default="", max_length=500, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("complete", "Complete"),
                            ("error", "Error"),
                            ("delete", "Delete"),
                            ("standby", "Stand By"),
                            ("no_file", "No File"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Work Process Master Data",
            },
        ),
        migrations.CreateModel(
            name="DatasetCycle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("metadata_url", models.URLField(blank=True, null=True)),
                ("description", models.JSONField(blank=True, null=True)),
                ("has_special_year_code", models.BooleanField(default=False)),
                (
                    "special_year_code",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("has_dataset", models.BooleanField(default=False)),
                (
                    "cycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.cycle"
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.dataset"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "06-Dataset by Cycle",
                "unique_together": {("dataset", "cycle")},
            },
        ),
        migrations.AddField(
            model_name="dataset",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nhanes.group"
            ),
        ),
        migrations.CreateModel(
            name="Logs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("system_version", models.CharField(default="0.1.4", max_length=15)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("e", "Error"), ("w", "Warning"), ("s", "Success")],
                        default="s",
                        max_length=1,
                    ),
                ),
                ("description", models.TextField(blank=True, default=None, null=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Logs",
            },
        ),
        migrations.CreateModel(
            name="NormalizedData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sample", models.IntegerField()),
                ("sequence", models.IntegerField(default=0)),
                ("value", models.CharField(max_length=255)),
                (
                    "cycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.cycle"
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.dataset"
                    ),
                ),
                (
                    "field",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.field"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Normalized Data",
            },
        ),
        migrations.CreateModel(
            name="QueryStructure",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("structure_name", models.CharField(max_length=100)),
                ("no_conflict", models.BooleanField(default=False)),
                ("no_multi_index", models.BooleanField(default=False)),
                (
                    "columns",
                    models.ManyToManyField(
                        related_name="query_columns", to="nhanes.querycolumns"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "08-Query Structure",
            },
        ),
        migrations.CreateModel(
            name="QueryFilter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "filter_name",
                    models.CharField(
                        choices=[
                            ("field__field", "Field Code"),
                            ("field__description", "Field Name"),
                            ("field__internal_id", "Field Internal Code"),
                            ("field__internal_group", "Field Internal Group"),
                            ("cycle__cycle", "Cycle"),
                            ("dataset__group__group", "Group"),
                            ("dataset__dataset", "Dataset Code"),
                            ("dataset__description", "Dataset Name"),
                        ],
                        default="variable",
                        max_length=30,
                    ),
                ),
                (
                    "operator",
                    models.CharField(
                        choices=[
                            ("eq", "Equal"),
                            ("ne", "Not Equal"),
                            ("lt", "Less Than"),
                            ("lte", "Less Than or Equal"),
                            ("gt", "Greater Than"),
                            ("gte", "Greater Than or Equal"),
                            ("contains", "Contains"),
                            ("icontains", "Contains (Case-Insensitive)"),
                            ("exact", "Exact"),
                            ("iexact", "Exact (Case-Insensitive)"),
                            ("in", "In"),
                            ("startswith", "Starts With"),
                            ("istartswith", "Starts With (Case-Insensitive)"),
                            ("endswith", "Ends With"),
                            ("iendswith", "Ends With (Case-Insensitive)"),
                            ("isnull", "Search For Null Values"),
                            ("search", "Search"),
                            ("regex", "Use Regular Expression"),
                            ("iregex", "Use Regular Expression (Case-Insensitive)"),
                            ("file", "Path to csv file with each value in a line"),
                        ],
                        default="eq",
                        max_length=20,
                    ),
                ),
                ("value", models.CharField(max_length=255)),
                (
                    "query_structure",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="filters",
                        to="nhanes.querystructure",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="field",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="features", to="nhanes.tag"
            ),
        ),
        migrations.CreateModel(
            name="RawData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sample", models.IntegerField()),
                ("sequence", models.IntegerField(default=0)),
                ("value", models.CharField(max_length=255)),
                (
                    "cycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.cycle"
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.dataset"
                    ),
                ),
                (
                    "variable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nhanes.variable",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "07-Data",
            },
        ),
        migrations.AlterUniqueTogether(
            name="dataset",
            unique_together={("dataset", "group")},
        ),
        migrations.CreateModel(
            name="NormalizationRule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rule", models.CharField(max_length=255, unique=True)),
                ("version", models.CharField(max_length=20)),
                ("folder_path", models.CharField(max_length=500)),
                ("file_name", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "destination_fields",
                    models.ManyToManyField(
                        related_name="destination_for_rules", to="nhanes.field"
                    ),
                ),
                (
                    "source_variables",
                    models.ManyToManyField(
                        related_name="source_for_rules", to="nhanes.variable"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Normalization Rules",
                "unique_together": {("rule", "version")},
            },
        ),
        migrations.CreateModel(
            name="VariableCycle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("variable_name", models.CharField(max_length=100)),
                ("sas_label", models.CharField(max_length=100)),
                ("english_text", models.TextField()),
                ("target", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
                ("value_table", models.JSONField()),
                (
                    "cycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.cycle"
                    ),
                ),
                (
                    "variable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nhanes.variable",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "05-Variable by Cycle",
                "indexes": [
                    models.Index(
                        fields=["variable", "cycle"],
                        name="nhanes_vari_variabl_59ffa1_idx",
                    )
                ],
                "unique_together": {("variable", "cycle")},
            },
        ),
        migrations.CreateModel(
            name="WorkProcess",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_download", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("complete", "Complete"),
                            ("error", "Error"),
                            ("delete", "Delete"),
                            ("standby", "Stand By"),
                            ("no_file", "No File"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("last_synced_at", models.DateTimeField(verbose_name="Last Update")),
                (
                    "source_file_version",
                    models.CharField(blank=True, default="", max_length=500, null=True),
                ),
                ("source_file_size", models.BigIntegerField(default=0)),
                (
                    "chk_raw",
                    models.BooleanField(
                        default=False, verbose_name="Raw Data Ingested"
                    ),
                ),
                (
                    "chk_normalization",
                    models.BooleanField(
                        default=False, verbose_name="Normalization Data Ingested"
                    ),
                ),
                ("system_version", models.CharField(default="0.1.4", max_length=15)),
                ("time_download", models.IntegerField(default=0)),
                ("time_raw", models.IntegerField(default=0)),
                ("time_normalization", models.IntegerField(default=0)),
                ("records_raw", models.IntegerField(default=0)),
                ("records_normalization", models.IntegerField(default=0)),
                ("n_samples", models.IntegerField(default=0)),
                ("n_variables", models.IntegerField(default=0)),
                (
                    "cycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.cycle"
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nhanes.dataset"
                    ),
                ),
                (
                    "datasetcycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nhanes.datasetcycle",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "06-Donwload Control",
                "unique_together": {("dataset", "cycle")},
            },
        ),
    ]
