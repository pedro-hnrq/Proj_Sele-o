# Generated by Django 4.1.5 on 2023-01-05 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='logo_empresa')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cidade', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=60)),
                ('nicho_mercado', models.CharField(choices=[('PB', 'ProgramadorBack-end'), ('PF', 'Programador|Font-end'), ('FS', 'FullStack'), ('M', 'Marketing'), ('N', 'Nutrição'), ('D', 'Design')], max_length=3)),
                ('caracteristica_empresa', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnologia', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('nivel_experiencia', models.CharField(choices=[('J', 'Júnior'), ('P', 'Pleno'), ('S', 'Sênior')], max_length=2)),
                ('data_final', models.DateField()),
                ('status', models.CharField(choices=[('I', 'Interesse'), ('C', 'Currículo enviado'), ('E', 'Entrevista'), ('D', 'Desafio técnico'), ('F', 'Finalizado')], max_length=30)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.empresa')),
                ('tecnologias_dominadas', models.ManyToManyField(to='empresa.tecnologias')),
                ('tecnologias_estudar', models.ManyToManyField(related_name='estudar', to='empresa.tecnologias')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='tecnologias',
            field=models.ManyToManyField(to='empresa.tecnologias'),
        ),
    ]
