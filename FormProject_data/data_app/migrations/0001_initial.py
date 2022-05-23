# Generated by Django 3.2.12 on 2022-05-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_uid', models.IntegerField(db_index=True)),
                ('form_name', models.CharField(max_length=150)),
                ('form_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=150)),
                ('field_description', models.CharField(blank=True, max_length=150, null=True)),
                ('field_char_type', models.CharField(blank=True, max_length=350, null=True)),
                ('field_text_type', models.TextField(blank=True, null=True)),
                ('field_selec_type', models.TextField(blank=True, null=True)),
                ('form_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='data_app.formmodels')),
            ],
        ),
    ]
