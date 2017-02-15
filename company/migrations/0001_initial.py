# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('company_website', models.URLField()),
                ('description', models.TextField()),
                ('company_logo', models.ImageField(blank=True, default='/static/images/company-logo.png', upload_to='company_logo')),
                ('contact_no', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('estabished_year', models.IntegerField(blank=True, null=True)),
                ('no_of_employes', models.IntegerField(blank=True, null=True)),
                ('mail_sent_to_company', models.NullBooleanField()),
            ],
        ),
    ]