# Generated by Django 4.2.6 on 2023-10-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_categoryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='our_services',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='cateqoriya adi'),
        ),
    ]
