# Generated by Django 4.2.13 on 2024-08-05 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryscience',
            options={'verbose_name': 'category Science', 'verbose_name_plural': 'category Science'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Kategorya'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categoryScience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryscience', verbose_name='Kategorya Fanlar'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='narxi'),
        ),
    ]
