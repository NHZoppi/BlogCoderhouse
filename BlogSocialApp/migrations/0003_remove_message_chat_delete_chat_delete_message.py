# Generated by Django 4.1.5 on 2023-01-31 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSocialApp', '0002_chat_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]