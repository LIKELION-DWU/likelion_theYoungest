# Generated by Django 4.2.2 on 2023-07-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postDiary', '0004_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='내용이 없습니다.', verbose_name='내용'),
        ),
    ]
