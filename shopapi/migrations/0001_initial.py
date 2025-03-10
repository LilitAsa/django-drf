# Generated by Django 5.1.6 on 2025-02-11 15:30

import django.core.validators
import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_hy', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Կատեգորիա',
                'verbose_name_plural': 'Կատեգորիաներ',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_hy', models.CharField(max_length=255, verbose_name='Հայերեն Վերնագիր։')),
                ('title_ru', models.CharField(max_length=255, verbose_name='Ռուսերեն Վերնագիր։')),
                ('title_en', models.CharField(max_length=255, verbose_name='Անգլերեն Վերնագիր։')),
                ('description_hy', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Հայերեն Նկարագրություն:')),
                ('description_ru', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Ռուսերեն Նկարագրություն:')),
                ('description_en', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Անգլերեն Նկարագրություն:')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Գլխավոր նկար:')),
                ('slug', models.SlugField(unique=True, verbose_name='Ցուցիչ:')),
                ('price', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('hidden', models.BooleanField(default=False)),
                ('reviews_qty', models.IntegerField(default=0)),
                ('stars_qty', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shopapi.category')),
            ],
            options={
                'verbose_name': 'Ապրանք',
                'verbose_name_plural': 'Ապրանքներ',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Ապրանքի նկար:')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapi.product', verbose_name='Ապրանքի Նկարներ։')),
            ],
            options={
                'verbose_name': 'Ապրանքի Նկար',
                'verbose_name_plural': 'Ապրանքի Նկարներ',
            },
        ),
    ]
