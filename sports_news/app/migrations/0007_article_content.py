# Generated by Django 5.1.6 on 2025-02-11 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_article_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
