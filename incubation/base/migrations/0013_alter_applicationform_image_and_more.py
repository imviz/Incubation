# Generated by Django 4.0.6 on 2022-07-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_applicationform_image_alter_applicationform_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.CharField(choices=[('approved', 'approved'), ('accept', 'accept'), ('pending', 'pending'), ('rejected', 'rejected')], default='pending', max_length=10),
        ),
    ]
