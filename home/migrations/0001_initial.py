# Generated by Django 4.1.3 on 2023-03-26 07:35

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("compname", models.CharField(max_length=120)),
                ("password", models.CharField(max_length=32)),
                ("category", models.CharField(max_length=64)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=120)),
                ("address", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=500)),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="company",
                        validators=[home.models.validate_file_extension],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
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
                ("name_Image", models.CharField(max_length=120)),
                (
                    "image",
                    models.ImageField(
                        upload_to="", validators=[home.models.validate_file_extension]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("compname", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=120)),
                ("category", models.CharField(max_length=120)),
                ("salary", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("type", models.CharField(max_length=32)),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="company",
                        validators=[home.models.validate_file_extension],
                    ),
                ),
                ("gpa", models.CharField(max_length=10)),
                ("description", models.CharField(max_length=500)),
                ("property", models.CharField(max_length=500)),
                ("welfare", models.CharField(max_length=500)),
                ("experience", models.CharField(max_length=32)),
                ("posted_date", models.DateTimeField()),
                ("working_time", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="JobApply",
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
                ("compname", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=64)),
                ("members", models.CharField(max_length=100)),
                ("apply_date", models.DateTimeField(auto_now_add=True)),
                ("member_id", models.IntegerField()),
                ("job_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Member",
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
                ("username", models.CharField(max_length=120)),
                ("password", models.CharField(max_length=32)),
                ("name_th", models.CharField(max_length=120)),
                ("name_eng", models.CharField(max_length=120)),
                ("birth_day", models.CharField(max_length=64)),
                ("sex", models.CharField(max_length=10)),
                ("nationality", models.CharField(max_length=32)),
                ("religion", models.CharField(max_length=64)),
                ("phone", models.CharField(max_length=10)),
                ("email", models.CharField(max_length=120)),
                ("school", models.CharField(max_length=120)),
                ("education_level", models.CharField(max_length=64)),
                ("faculty", models.CharField(max_length=120)),
                ("major", models.CharField(max_length=120)),
                ("education_category", models.CharField(max_length=64)),
                ("state", models.CharField(max_length=32)),
                ("year", models.CharField(max_length=10)),
                ("gpa", models.CharField(max_length=10)),
                (
                    "application_form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.company"
                    ),
                ),
            ],
        ),
    ]