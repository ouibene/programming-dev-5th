# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 04:02
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160801_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.IntegerField(validators=[blog.validators.ZipCodeValidator()])),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number1',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
    ]
