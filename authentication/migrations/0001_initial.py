# Generated by Django 4.1.7 on 2023-02-20 06:52

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
            name='KYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('SSN', 'SSN'), ('PASSPORT', 'PASSPORT'), ('DRIVING_LICENSE', 'DRIVING_LICENSE')], default='SSN', max_length=20)),
                ('id_number', models.IntegerField()),
                ('doc_front_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('doc_back_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('doc_selfie', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
