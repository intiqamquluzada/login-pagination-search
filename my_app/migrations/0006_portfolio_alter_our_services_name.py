# Generated by Django 4.2.6 on 2023-10-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_remove_categoryimage_our_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='our_services',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='servis adi'),
        ),
    ]
