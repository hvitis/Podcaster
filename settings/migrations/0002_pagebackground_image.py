# Generated by Django 3.0 on 2019-12-18 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagebackground',
            name='image',
            field=models.ImageField(blank=True, help_text='This will be page bacground.', null=True, upload_to='backgrounds/'),
        ),
    ]
