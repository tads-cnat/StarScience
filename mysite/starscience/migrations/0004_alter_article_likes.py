# Generated by Django 4.1.3 on 2023-01-19 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starscience', '0003_alter_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
