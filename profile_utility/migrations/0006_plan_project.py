# Generated by Django 4.1.2 on 2024-04-19 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_utility', '0005_itemlist_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_utility.post'),
        ),
    ]
