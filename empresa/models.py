from datetime import date, timezone
import datetime
from django.db import models


class Tecnologias(models.Model):
    logo_tecn = models.ImageField(upload_to="logo_tecn", null=True)
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'

class Profissao(models.Model):
    logo_profissao = models.ImageField(upload_to="logo_tecn", null=True)
    profissao = models.CharField(max_length=50)

    def __str__(self):
        return self.profissao 
    
    class Meta:
        verbose_name = 'Profissao'
        verbose_name_plural = 'Profissoes'

class Empresa(models.Model):    
    
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=18)
    email = models.EmailField()
    caracteristica_empresa = models.TextField()
    
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    
    
   
    tecnologias = models.ManyToManyField(Tecnologias)
    profissao_empresa = models.ManyToManyField(Profissao) 
    
    def __str__(self):
        return self.nome

    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()

   

class Vagas(models.Model):
    tipo_experiencia = (
        ('TE', 'Trainee/Estagiário'),
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior'),
        ('E', 'Especialista'),
        ('L', 'Líder')
    )
    
    tipo_trabalho = (
        ('P', 'Presencial'),
        ('H', 'Híbrido'),
        ('R', 'Remoto'),
    )
    
    tipo_contratacao = (
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
    )

    # choices_status = (
    #     ('I', 'Interesse'),
    #     ('C', 'Currículo enviado'),
    #     ('E', 'Entrevista'),
    #     ('D', 'Desafio técnico'),
    #     ('F', 'Finalizado')
    # )
    # titulo = models.CharField(max_length=30)

    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    
    data_inicial = models.DateField(default=date.today)
    data_final = models.DateField()
    
    nivel_experiencia = models.CharField(max_length=2, choices=tipo_experiencia)
    trabalho = models.CharField(max_length=3, choices=tipo_trabalho)
    contratacao = models.CharField(max_length=3, choices=tipo_contratacao)
    
    profissao_vaga = models.ForeignKey(Profissao, null=True, on_delete=models.SET_NULL)
    tecnologia_vaga = models.ManyToManyField(Tecnologias, related_name='estudar')
   
    # status = models.CharField(max_length=30, choices=choices_status)
    # tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    # tecnologias_estudar = models.ManyToManyField(
    #     Tecnologias, related_name='estudar')

    def remuneracao(self):
        return f"R$ {self.remuneracao_profissional:.2f}"

    remuneracao_profissional = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.data_inicial < timezone.now().date():
            raise ValueError("Data inicial não pode ser anterior à data atual.")
        super(Vagas, self).save(*args, **kwargs)




    # Tem como fazer a BARRA DE PROGRESSÃO 2 formas
    def progresso(self):

        # 1 forma
        
        # if self.status == "I":
        #     return 20
        # elif self.status == "C":
        #     return 40
        # elif self.status == "E":
        #     return 60
        # elif self.status == "D":
        #     return 80
        # elif self.status == "F":
        #     return 100

        # 2 Forma
        x = [((i+1)*20, j[0]) for i, j in enumerate(self.choices_status)]
        x = list(filter(lambda x: x[1] == self.status, x))[0][0]
        return x

    def __str__(self):
        return self.empresa

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
