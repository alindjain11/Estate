# Generated by Django 2.1.2 on 2018-12-20 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showall',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Seller.Seller'),
        ),
    ]