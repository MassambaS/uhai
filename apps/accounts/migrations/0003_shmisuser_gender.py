# Generated by Django 4.2.7 on 2023-12-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_shmisuser_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='shmisuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Mâle'), ('F', 'Femâle')], default='M', max_length=1),
        ),
    ]
