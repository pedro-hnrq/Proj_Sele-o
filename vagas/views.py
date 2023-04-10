from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from empresa.models import Vagas, Profissao
from .models import Tarefa, Emails
from django.contrib import messages
from django.contrib.messages import constants
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import datetime


def nova_vaga(request):
    if request.method == "POST":
        # titulo = request.POST.get('titulo')
        empresa = request.POST.get('empresa')
        email = request.POST.get('email').strip()  # removendo espaços antes e depois do email
        
        data_inicial = request.POST.get('data_inicial')
        data_final = request.POST.get('data_final')        
        # Converter data_inicial e data_final para objetos datetime.date
        data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d').date()
        data_final = datetime.strptime(data_final, '%Y-%m-%d').date()
                
        profissao = request.POST.get('profissao')
        profissao_obj = Profissao.objects.get(nome=profissao)
        tecnologia = request.POST.getlist('tecnologia')
        
        
        experiencia = request.POST.get('experiencia')        
        tipo_trabalho = request.POST.get('tipo_trabalho')
        contratacao = request.POST.get('contratacao')
        # status = request.POST.get('status')

        salario = request.POST.get('salario')
        # convertendo salario para lambda com formatação
        valor_salario = "{:,.2f}".format(float(salario)) if salario else None

        
         # Obter a data atual
        data_atual = datetime.today().date()
         # Verificar se a data inicial está entre a data atual e a data final
        if not (data_atual <= data_inicial <= data_final):
            messages.add_message(request, constants.ERROR, 'A data inicial deve estar entre a data atual e a data final.')
            return redirect('empresa_unica')
        
        
        if Vagas.objects.filter(email=email).exists():  # verificando se já existe email cadastrado
            messages.add_message(request, constants.ERROR, 'Email já cadastrado.')
            return redirect('empresa_unica')
        
        
        
        vaga = Vagas(empresa=empresa,
                     email=email,                     
                     data_inicial=data_inicial,
                     data_final=data_final,
                     profissao_vaga = profissao_obj,
                     tecnologia_vaga = tecnologia,
                     nivel_experiencia=experiencia,
                     trabalho=tipo_trabalho,
                     contratacao=contratacao,
                     remuneracao_profissional=valor_salario,   
                    )

        vaga.save()

        # vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        # vaga.tecnologias_dominadas.add(*tecnologias_domina)

        # vaga.save()

        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresa/{empresa}')

    elif request.method == "GET":
        raise Http404()

def vaga(request, id):
    vaga = get_object_or_404(Vagas, id=id)
    tarefas = Tarefa.objects.filter(vaga=vaga).filter(realizada=False)
    emails = Emails.objects.filter(vaga=vaga)
    return render(request, 'vaga.html', {'vaga': vaga,
                                         'tarefas': tarefas,
                                         'emails': emails,})

def nova_tarefa(request, id_vaga):

    titulo = request.POST.get('titulo')
    prioridade = request.POST.get("prioridade")
    data = request.POST.get('data')

    if (len(titulo.strip()) == 0 or len(prioridade.strip()) == 0 or len(data.strip()) == 0): 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect(f'/vagas/vaga/{id_vaga}')
    try:
        tarefa = Tarefa(vaga_id=id_vaga,
                        titulo=titulo,
                        prioridade=prioridade,
                        data=data)
        tarefa.save()
        messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno no sistema.')
        return redirect(f'/vagas/vaga/{id_vaga}')

def realizar_tarefa(request, id):
    tarefas_list = Tarefa.objects.filter(id=id).filter(realizada=False)

    if not tarefas_list.exists():
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/home/empresas/')

    tarefa = tarefas_list.first()
    tarefa.realizada = True
    tarefa.save()    
    messages.add_message(request, constants.SUCCESS, 'Tarefa realizada com sucesso, parabéns!')
    return redirect(f'/vagas/vaga/{tarefa.vaga.id}')

def envia_email(request, id_vaga):
    vaga = Vagas.objects.get(id=id_vaga)
    assunto = request.POST.get('assunto')
    corpo = request.POST.get('corpo')

    html_content = render_to_string('emails/template_email.html', {'corpo': corpo})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, [vaga.email,])
    email.attach_alternative(html_content, "text/html")
    if email.send():
        mail = Emails(
            vaga=vaga, 
            assunto=assunto,
            corpo=corpo,
            enviado=True
        )
        mail.save()  
        messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso.')
        return redirect(f'/vagas/vaga/{id_vaga}')
    else:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/vagas/vaga/{id_vaga}')