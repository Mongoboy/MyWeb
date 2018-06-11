# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-06 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SitesApp', '0007_auto_20180606_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatrecord',
            name='crIP',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='电脑IP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uAge',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uDateTime',
            field=models.DateTimeField(auto_now=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uEmail',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uGender',
            field=models.NullBooleanField(default=None, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uIP',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='电脑IP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uIcon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uName',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uNickName',
            field=models.CharField(default='guest', max_length=20, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uPwd',
            field=models.CharField(default=None, max_length=32, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uToken',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, unique=True, verbose_name='登录状态'),
        ),
    ]