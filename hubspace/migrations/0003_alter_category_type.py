# Generated by Django 5.1.5 on 2025-03-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspace', '0002_alter_post_content_alter_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(default='jokes', max_length=7),
        ),
    ]
