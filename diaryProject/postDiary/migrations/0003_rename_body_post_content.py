# Generated by Django 4.2.2 on 2023-07-03 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postDiary', '0002_alter_post_titledate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
    ]
