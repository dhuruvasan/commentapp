# Generated by Django 3.1.2 on 2022-02-09 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
