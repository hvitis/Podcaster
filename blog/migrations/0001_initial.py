# Generated by Django 3.0 on 2019-12-19 02:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, help_text='SEO Title appearing in search engines.', max_length=250, null=True)),
                ('meta_description', models.CharField(blank=True, help_text='SEO Description appearing in search engines.', max_length=250, null=True)),
                ('meta_keywords', models.CharField(blank=True, help_text='SEO Keywords helping in users searches.', max_length=250)),
                ('title', models.CharField(max_length=199)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, help_text='Created automatically, no need to fill.', max_length=250)),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(blank=True, default='blog/default.jpeg', help_text='This picture will be uploaded to AWS.', null=True, upload_to='blog/')),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
    ]
