# Generated by Django 4.1.7 on 2023-04-04 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0007_profissao_remove_empresa_nicho_empresa_delete_nicho_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profissao',
            old_name='logo_tecn',
            new_name='logo_profissao',
        ),
    ]
