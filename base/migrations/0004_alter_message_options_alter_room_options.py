# Generated by Django 4.2.1 on 2024-07-20 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]