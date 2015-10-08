# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20151004_0445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('sales_date', models.DateTimeField()),
                ('customer_id', models.ForeignKey(to='product.Customer')),
                ('product_id', models.ForeignKey(to='product.Product')),
            ],
        ),
    ]
