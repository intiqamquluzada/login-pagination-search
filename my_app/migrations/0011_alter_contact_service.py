# Generated by Django 4.2.6 on 2023-10-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_alter_about_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='service',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='xidmet'),
        ),
    ]
