# Generated by Django 5.1.5 on 2025-03-16 22:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspace', '0003_alter_category_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=270),
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='react', to='hubspace.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='react', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
