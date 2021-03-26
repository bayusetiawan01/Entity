# Generated by Django 3.1.7 on 2021-03-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendaftaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('npm', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('motivasi', models.CharField(max_length=1024)),
                ('menjadi_pengurus', models.BooleanField(default=1)),
                ('minat', models.CharField(max_length=50)),
                ('hari', models.CharField(max_length=50)),
                ('bahasa', models.CharField(max_length=50)),
                ('harapan', models.CharField(max_length=50)),
                ('dd_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='created_at',
            new_name='dd_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='code',
        ),
    ]
