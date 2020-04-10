# Generated by Django 2.2 on 2020-04-10 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20191219_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageOGTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('select', 'SELECT'), ('home', 'HOME'), ('about', 'ABOUT'), ('episodes', 'EPISODES'), ('blog', 'BLOG'), ('contact', 'CONTACT')], default='select', max_length=25, unique=True)),
                ('image', models.ImageField(blank=True, help_text='This will be page bacground.', null=True, upload_to='backgrounds/')),
            ],
            options={
                'verbose_name': 'Page Backgrounds',
                'verbose_name_plural': 'Page Backgrounds',
            },
        ),
        migrations.AlterField(
            model_name='pagedescription',
            name='name',
            field=models.CharField(choices=[('select', 'SELECT'), ('title', 'TITLE'), ('description', 'DESCRIPTION'), ('website_url', 'WEBSITE_URL')], default='select', max_length=25, unique=True),
        ),
    ]
