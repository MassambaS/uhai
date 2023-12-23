# Generated by Django 4.2.7 on 2023-12-23 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'counties',
            },
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'parishes',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('badge', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('PRIMARY', 'Primary school'), ('SECONDARY', 'Upper secondary')], max_length=10)),
                ('ownership', models.CharField(choices=[('GOV', 'Governement'), ('PRIV', 'Private')], max_length=4)),
                ('type', models.CharField(choices=[('DAY', 'Day'), ('BOARDING', 'Boarding'), ('DAY_BOARDING', 'Day & Boarding')], max_length=12)),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=250)),
                ('last_name', models.CharField(blank=True, max_length=250)),
                ('gender', models.CharField(choices=[('M', 'Mâle'), ('F', 'Femâle')], default='M', max_length=1)),
                ('date_of_birth', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('key', models.CharField(blank=True, max_length=15, unique=True)),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.parish')),
            ],
            options={
                'db_table': 'villages',
            },
        ),
        migrations.CreateModel(
            name='Sub_county',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.county')),
            ],
            options={
                'db_table': 'subCounties',
            },
        ),
        migrations.CreateModel(
            name='StudentSchoolHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('level', models.CharField(choices=[('PRIMARY', 'Primary school'), ('SECONDARY', 'Upper secondary')], max_length=10)),
                ('year', models.CharField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth')], max_length=1)),
                ('success', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='schools.school')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='schools.students')),
            ],
            options={
                'db_table': 'students_school_history',
            },
        ),
        migrations.AddField(
            model_name='school',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.village'),
        ),
        migrations.AddField(
            model_name='parish',
            name='sub_county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.sub_county'),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('region', models.CharField(choices=[('EAST', 'Eastern regions'), ('WEST', 'Western regions'), ('NORTH', 'Northern regions'), ('SOUTH', 'Southern regions'), ('CENTRAL', 'Central regions')], max_length=7)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.country')),
            ],
            options={
                'db_table': 'districts',
            },
        ),
        migrations.AddField(
            model_name='county',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.district'),
        ),
    ]