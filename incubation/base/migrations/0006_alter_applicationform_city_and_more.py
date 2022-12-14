# Generated by Django 4.0.6 on 2022-07-21 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_applicationform_slot_alter_applicationform_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='mobile',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='state',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('accept', 'accept'), ('pending', 'pending'), ('approved', 'approved')], default='pending', max_length=10),
        ),
        migrations.CreateModel(
            name='SlotBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=30)),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.applicationform')),
            ],
        ),
    ]
