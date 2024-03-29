# Generated by Django 5.0.1 on 2024-01-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_description_users_phone_users_portfolio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='username',
            field=models.CharField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, null=True, unique=True),
        ),
    ]
