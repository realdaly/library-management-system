# Generated by Django 4.2.2 on 2023-07-08 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('author_img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'متوفر'), ('borrowed', 'مستعار'), ('sold', 'مباع')], max_length=50, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lms_app.category')),
            ],
        ),
    ]
