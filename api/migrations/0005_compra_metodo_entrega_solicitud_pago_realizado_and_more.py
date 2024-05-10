# Generated by Django 5.0.6 on 2024-05-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_producto_id_alter_producto_codigoproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='metodo_entrega',
            field=models.CharField(choices=[('D', 'Despacho a Domicilio'), ('R', 'Retiro en Tienda')], default='Despacho a Domicilio', max_length=1),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='pago_realizado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='estado_pedido',
            field=models.CharField(choices=[('P', 'Pedido en Proceso'), ('R', 'Pedido rechazado'), ('E', 'Pedido enviado'), ('D', 'Pedido Despachado')], max_length=1),
        ),
    ]
