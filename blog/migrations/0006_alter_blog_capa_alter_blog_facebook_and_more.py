# Generated by Django 5.1.2 on 2024-11-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_logo_blog_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='capa',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='twitter',
            field=models.URLField(blank=True),
        ),
    ]