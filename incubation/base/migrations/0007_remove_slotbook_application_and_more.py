# Generated by Django 4.0.6 on 2022-07-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_applicationform_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotbook',
            name='application',
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.CharField(choices=[('accept', 'accept'), ('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], default='pending', max_length=10),
        ),
    ]
