# Generated by Django 4.1 on 2023-01-03 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='дата лайка')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
        migrations.CreateModel(
            name='PostDelay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Время отложенной публикации')),
            ],
            options={
                'verbose_name': 'Отложенная задача',
                'verbose_name_plural': 'Отложенные задачи',
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='название тега')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='UserView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='дата просмотра')),
                ('client_ip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.clientip', verbose_name='IP пользователя')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Просмотр пользователя',
                'verbose_name_plural': 'Просмотры пользователей',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='дата публикации')),
                ('only_for_adult', models.BooleanField(default=False, verbose_name='18+ контент')),
                ('for_autenticated_users', models.BooleanField(default=False, verbose_name='для авторизированных пользователей')),
                ('disable_comments', models.BooleanField(default=False, verbose_name='запретить коментарии')),
                ('status', models.CharField(choices=[('PB', 'опубликовано'), ('DF', 'отложено'), ('CN', 'на рассмотрении')], default='CN', help_text='При выборе задержки помечается как "отложено"', max_length=20, verbose_name='статус')),
                ('description', models.CharField(blank=True, max_length=1500, null=True, verbose_name='описание')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('delay', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.postdelay', verbose_name='время отложенной публикации')),
                ('likes', models.ManyToManyField(blank=True, to='posts.like', verbose_name='лайки')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='posts.posttag', verbose_name='теги')),
                ('views', models.ManyToManyField(blank=True, to='posts.userview')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
                'ordering': ('-creation_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text', models.TextField(verbose_name='текст')),
                ('answered', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_comments', to='posts.comment', verbose_name='Комментируемый комментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post', verbose_name='комментируемый пост')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ('-pub_date',),
            },
        ),
    ]
