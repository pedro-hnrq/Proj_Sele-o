from django.db import models


class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'


class Empresa(models.Model):
    choices_nicho_mercado = (
        ('PB', 'Programador | Back-end'),
        ('PF', 'Programador | Font-end'),
        ('FS', 'FullStack'),
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
    )
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=5, blank=True)
    tecnologias = models.ManyToManyField(Tecnologias)
    nicho_mercado = models.CharField(
        max_length=3, choices=choices_nicho_mercado)
    caracteristica_empresa = models.TextField()

    def __str__(self):
        return self.nome

    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()


class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )

    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(
        max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    email = models.EmailField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(
        Tecnologias, related_name='estudar')

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
        return self.titulo

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
