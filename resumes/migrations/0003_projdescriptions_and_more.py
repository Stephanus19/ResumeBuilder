# Generated by Django 4.1.4 on 2022-12-14 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resumes", "0002_projectdescriptions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjDescriptions",
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
                ("proj_description", models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name="jobdescriptions",
            old_name="description",
            new_name="job_description",
        ),
        migrations.RemoveField(
            model_name="employment",
            name="descriptions",
        ),
        migrations.RemoveField(
            model_name="projects",
            name="descriptions",
        ),
        migrations.RemoveField(
            model_name="resume",
            name="education",
        ),
        migrations.RemoveField(
            model_name="resume",
            name="employment",
        ),
        migrations.RemoveField(
            model_name="resume",
            name="projects",
        ),
        migrations.RemoveField(
            model_name="resume",
            name="skills",
        ),
        migrations.AddField(
            model_name="education",
            name="resume",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="education",
                to="resumes.resume",
            ),
        ),
        migrations.AddField(
            model_name="employment",
            name="employment_descriptions",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employer",
                to="resumes.jobdescriptions",
            ),
        ),
        migrations.AddField(
            model_name="employment",
            name="resume",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employment",
                to="resumes.resume",
            ),
        ),
        migrations.AddField(
            model_name="jobdescriptions",
            name="employment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jobdescriptions",
                to="resumes.employment",
            ),
        ),
        migrations.AddField(
            model_name="projects",
            name="resume",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="resumes.resume",
            ),
        ),
        migrations.AddField(
            model_name="skills",
            name="resume",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="skills",
                to="resumes.resume",
            ),
        ),
        migrations.DeleteModel(
            name="ProjectDescriptions",
        ),
        migrations.AddField(
            model_name="projdescriptions",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projdescriptions",
                to="resumes.projects",
            ),
        ),
        migrations.AddField(
            model_name="projects",
            name="project_descriptions",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="resumes.projdescriptions",
            ),
        ),
    ]
