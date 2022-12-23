# Generated by Django 4.1 on 2022-12-21 19:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediacore', '0010_alter_imagefile_file_alter_videofile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='file',
            field=models.ImageField(upload_to='post_media/2022/12/21', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'png', 'gif', 'webp'))], verbose_name='файл'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='file',
            field=models.FileField(upload_to='post_media/2022/12/21', verbose_name='файл'),
        ),
    ]
