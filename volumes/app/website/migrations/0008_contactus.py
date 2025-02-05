# Generated by Django 4.2.18 on 2025-02-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_website_socialmedias_socials_interestedin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
