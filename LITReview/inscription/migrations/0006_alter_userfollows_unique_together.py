# Generated by Django 4.0.1 on 2022-01-26 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0005_alter_userfollows_unique_together_user_follow_profil'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together={('user', 'followed_user')},
        ),
    ]
