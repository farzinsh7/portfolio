# Generated by Django 3.2 on 2023-09-08 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MySkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=100)),
                ('class_icon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=150)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('logo_image', models.ImageField(null=True, upload_to='logo')),
                ('fav_icon', models.ImageField(null=True, upload_to='fav-icon')),
                ('address', models.CharField(max_length=400)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('happy_client', models.IntegerField(null=True)),
                ('projects_count', models.IntegerField(null=True)),
                ('hours_of_support', models.IntegerField(null=True)),
                ('awards', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('icon', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('site_setting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='socials', to='portfolio_settings.sitesetting')),
            ],
        ),
    ]
