# Generated by Django 2.1.3 on 2018-11-25 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('momofit', '0006_auto_20181125_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='user_id',
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menu',
            name='user',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
