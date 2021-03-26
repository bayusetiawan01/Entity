# Generated by Django 3.1.7 on 2021-03-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210327_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='deskripsi',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='gambar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pendaftaran',
            name='bahasa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pendaftaran',
            name='harapan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pendaftaran',
            name='hari',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pendaftaran',
            name='minat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pendaftaran',
            name='motivasi',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
