# Generated by Django 5.0.6 on 2024-06-21 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scope_options_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main', 'tag__name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
