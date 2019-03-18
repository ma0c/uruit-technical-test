# Generated by Django 2.1.7 on 2019-03-18 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190318_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='player1_move',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1_move', to='core.GameMove'),
        ),
        migrations.AlterField(
            model_name='round',
            name='player2_move',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2_move', to='core.GameMove'),
        ),
    ]
