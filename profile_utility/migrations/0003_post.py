# Generated by Django 4.1.2 on 2024-04-11 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_utility', '0002_alter_customuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='POST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_utility.customuser')),
            ],
        ),
    ]
