# Generated by Django 3.2.4 on 2021-08-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[("Farg'ona", 'fergana'), ('Namangan', 'namangan'), ('Andijon', 'andijan')], max_length=50, verbose_name='Viloyat'),
        ),
    ]
