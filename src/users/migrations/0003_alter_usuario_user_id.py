# Generated by Django 4.2.3 on 2023-07-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_usuario_id_usuario_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='user_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
