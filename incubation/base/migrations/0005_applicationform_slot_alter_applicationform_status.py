# Generated by Django 4.0.6 on 2022-07-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_applicationform_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationform',
            name='slot',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('approved', 'approved'), ('pending', 'pending'), ('accept', 'accept')], default='pending', max_length=10),
        ),
    ]
