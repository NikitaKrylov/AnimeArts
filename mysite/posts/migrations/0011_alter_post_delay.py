# Generated by Django 4.1 on 2022-11-27 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_postdelay_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='delay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.postdelay', verbose_name='время отложенной публикации'),
        ),
    ]
