# Generated by Django 4.1 on 2023-01-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users_avatars/', verbose_name='иконка пользователя'),
        ),
    ]
