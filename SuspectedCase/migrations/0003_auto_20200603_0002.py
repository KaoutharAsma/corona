# Generated by Django 3.0.6 on 2020-06-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuspectedCase', '0002_suspectedcase_reporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspectedcase',
            name='attachment',
            field=models.FileField(blank=True, default=None, max_length=500, null=True, upload_to='attachment'),
        ),
    ]