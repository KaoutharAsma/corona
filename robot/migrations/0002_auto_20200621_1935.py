# Generated by Django 3.0.6 on 2020-06-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robotyoutube',
            name='image',
        ),
        migrations.AddField(
            model_name='robotyoutube',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'pending'), (2, 'accepted'), (3, 'rejected')], default=1),
        ),
        migrations.AlterField(
            model_name='robotyoutube',
            name='thumb',
            field=models.CharField(max_length=255),
        ),
    ]