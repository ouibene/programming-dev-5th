# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 08:08
from __future__ import unicode_literals

import blog.fields
import blog.models
import blog.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number1', blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='anonymous', max_length=20)),
                ('title', models.CharField(max_length=100, validators=[blog.models.MinLengthValidator(2)], verbose_name='제목')),
                ('content', models.TextField(help_text='Markdown 문법을 써주세요.')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('test_field', models.IntegerField(default=10)),
                ('lnglat', models.CharField(help_text='위도,경도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator])),
                ('phone', models.CharField(max_length=20, validators=[blog.validators.phone_number_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
