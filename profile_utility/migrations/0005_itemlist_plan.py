# Generated by Django 4.1.2 on 2024-04-18 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_utility', '0004_rename_description_post_company_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('total_floors', models.CharField(blank=True, max_length=255, null=True)),
                ('no_of_employees', models.CharField(blank=True, max_length=255, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_utility.post')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_or_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_utility.itemlist')),
            ],
        ),
    ]
