# Generated by Django 4.2.18 on 2025-02-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_myinformation_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinformation',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='myinformation',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='socialmedias',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='socialmedias',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='website',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
