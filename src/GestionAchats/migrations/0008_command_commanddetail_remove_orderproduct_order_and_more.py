# Generated by Django 4.1.4 on 2023-01-21 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAchats', '0007_order_orderproduct_delete_command_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAchats.client')),
            ],
        ),
        migrations.CreateModel(
            name='CommandDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAchats.command')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAchats.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]