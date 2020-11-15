# Generated by Django 3.1.3 on 2020-11-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birthdate',
            field=models.DateField(blank=True, help_text='Date of birth', null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
