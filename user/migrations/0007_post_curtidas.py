# Generated by Django 5.0.3 on 2024-06-19 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='curtidas',
            field=models.IntegerField(default=0),
        ),
    ]
