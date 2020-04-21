# Generated by Django 2.2 on 2020-04-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_auto_20200410_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagebackground',
            name='name',
            field=models.CharField(choices=[('select', 'SELECT'), ('home', 'HOME'), ('about', 'ABOUT'), ('podcasts', 'PODCASTS'), ('blog', 'BLOG'), ('contact', 'CONTACT')], default='select', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='pageogtags',
            name='name',
            field=models.CharField(choices=[('select', 'SELECT'), ('home', 'HOME'), ('about', 'ABOUT'), ('podcasts', 'PODCASTS'), ('blog', 'BLOG'), ('contact', 'CONTACT')], default='select', max_length=25, unique=True),
        ),
    ]