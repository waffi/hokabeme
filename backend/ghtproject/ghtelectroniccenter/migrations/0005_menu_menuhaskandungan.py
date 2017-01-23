# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-01-06 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ghtelectroniccenter', '0004_akumakan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('id_kategori', models.IntegerField(default=0)),
                ('nama_menu', models.CharField(max_length=50)),
                ('harga_menu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MenuHasKandungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kandungan', models.IntegerField(default=0)),
                ('kandungan', models.CharField(max_length=50)),
                ('id_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghtelectroniccenter.Menu')),
            ],
        ),
    ]
