# Generated by Django 5.0 on 2024-03-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='share_with',
            field=models.CharField(blank=True, choices=[('private', 'private'), ('public', 'public')], max_length=255, null=True),
        ),
    ]
