# Generated by Django 5.1.1 on 2025-02-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User'), ('OPERATOR', 'Operator')], default='USER', max_length=20),
        ),
    ]
