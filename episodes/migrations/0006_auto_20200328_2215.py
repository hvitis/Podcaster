# Generated by Django 2.2 on 2020-03-28 22:15

from django.db import migrations, models
import episodes.models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0005_auto_20200328_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ('-publish',), 'verbose_name': 'Podcasts', 'verbose_name_plural': 'Podcasts'},
        ),
        migrations.AlterField(
            model_name='episode',
            name='audio',
            field=models.FileField(upload_to=episodes.models.custom_route),
        ),
        migrations.AlterField(
            model_name='episode',
            name='background',
            field=models.ImageField(blank=True, help_text='This picture will be uploaded to AWS.', null=True, upload_to=episodes.models.custom_route),
        ),
        migrations.AlterField(
            model_name='episode',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='This picture will be uploaded to AWS.', null=True, upload_to=episodes.models.custom_route),
        ),
    ]
