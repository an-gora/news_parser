# Generated by Django 4.0.4 on 2022-05-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_news_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=150)),
            ],
        ),
    ]