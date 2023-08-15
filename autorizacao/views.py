from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from .models import Autorizacao
from django.core import serializers
import json
from django.shortcuts import get_object_or_404
from fpdf import FPDF
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url="/auth/login/")
def autorizacao(request):
    if request.method == "GET":
        autorizacoes_list = Autorizacao.objects.all()
        return render(request, 'autorizacao.html', {'autorizacoes': autorizacoes_list})
    elif request.method == "POST":
        categoria = request.POST.get('categoria')
        tipo = request.POST.get('tipo')
        numero = request.POST.get('numero')
        emissao = request.POST.get('emissao')
        validade = request.POST.get('validade')
        proc_ADM = request.POST.get('proc_ADM')
        tcaNum = request.POST.get('tcaNum')
        compromitente = request.POST.get('compromitente')
        cpfcnpj = request.POST.get('cpfcnpj')
        insc_CAD = request.POST.get('insc_CAD')
        endereco = request.POST.get('endereco')
        quadra = request.POST.get('quadra')
        lote = request.POST.get('lote')
        bairro = request.POST.get('bairro')
        area_lote = request.POST.get('area_lote')
        sup_aut = request.POST.get('sup_aut')
        matricula = request.POST.get('matricula')
        anuencia_CETESB = request.POST.get('anuencia_CETESB')
        anuencia_CONDEMA = request.POST.get('anuencia_CONDEMA')
        compensacao_averbacao = request.POST.get('compensacao_averbacao')
        observacao = request.POST.get('observacao')
        objetivo = request.POST.get('objetivo')
        local = request.POST.get('local')
        nativos = request.POST.get('nativos')
        exoticos = request.POST.get('exoticos')
        euterpe = request.POST.get('euterpe')
        transplante = request.POST.get('transplante')
        vegetacao = request.POST.get('vegetacao')
        estagio = request.POST.get('estagio')
        area_aut = request.POST.get('area_aut')
        recup_PRAD = request.POST.get('recup_PRAD')
        app1 = request.POST.get('app1')
        app2 = request.POST.get('app2')
        reserva = request.POST.get('reserva')
        restricao = request.POST.get('restricao')
        area_rest = request.POST.get('area_rest')

        autorizacao = Autorizacao.objects.filter(numero=numero)

        if autorizacao.exists():
            messages.info(request, 'Autorização já existe. Atualize-a')
            return render(request, 'listar_autorizacao.html')

        autorizacao = Autorizacao(
            categoria=categoria,
            tipo=tipo,
            numero=numero,
            emissao=emissao,
            validade=validade,
            proc_ADM=proc_ADM,
            tcaNum=tcaNum,
            compromitente=compromitente,
            cpfcnpj=cpfcnpj,
            insc_CAD=insc_CAD,
            endereco=endereco,
            quadra=quadra,
            lote=lote,
            bairro=bairro,
            area_lote=area_lote,
            sup_aut=sup_aut,
            matricula=matricula,
            anuencia_CETESB=anuencia_CETESB,
            anuencia_CONDEMA=anuencia_CONDEMA,
            compensacao_averbacao=compensacao_averbacao,
            observacao=observacao,
            objetivo=objetivo,
            local=local,
            nativos=nativos,
            exoticos=exoticos,
            euterpe=euterpe,
            transplante=transplante,
            vegetacao=vegetacao,
            estagio=estagio,
            area_aut=area_aut,
            recup_PRAD=recup_PRAD,
            app1=app1,
            app2=app2,
            reserva=reserva,
            restricao=restricao,
            area_rest=area_rest,
        )

        autorizacao.save()

        messages.info(request, 'Autorização cadastrada com sucesso!')
        return render(request, 'pagina_inicial.html')


@login_required(login_url="/auth/login/")
def att_autorizacao(request):
    id_autorizacao = request.POST.get('id_autorizacao')
    autorizacao = Autorizacao.objects.filter(id=id_autorizacao)
    autorizacao_json = json.loads(serializers.serialize('json', autorizacao))[0]['fields']
    autorizacao_id = json.loads(serializers.serialize('json', autorizacao))[0]['pk']
    data = {'autorizacao': autorizacao_json, 'autorizacao_id': autorizacao_id}
    return JsonResponse(data)


@login_required(login_url="/auth/login/")
def update_autorizacao(request, id):
    body = json.loads(request.body)

    categoria = body['categoria']
    tipo = body['tipo']
    numero = body['numero']
    emissao = body['emissao']
    validade = body['validade']
    proc_ADM = body['proc_ADM']
    tcaNum = body['tcaNum']
    compromitente = body['compromitente']
    cpfcnpj = body['cpfcnpj']
    insc_CAD = body['insc_CAD']
    endereco = body['endereco']
    quadra = body['quadra']
    lote = body['lote']
    bairro = body['bairro']
    area_lote = body['area_lote']
    sup_aut = body['sup_aut']
    matricula = body['matricula']
    anuencia_CETESB = body['anuencia_CETESB']
    anuencia_CONDEMA = body['anuencia_CONDEMA']
    compensacao_averbacao = body['compensacao_averbacao']
    observacao = body['observacao']
    objetivo = body['objetivo']
    local = body['local']
    nativos = body['nativos']
    exoticos = body['exoticos']
    euterpe = body['euterpe']
    transplante = body['transplante']
    vegetacao = body['vegetacao']
    estagio = body['estagio']
    area_aut = body['area_aut']
    recup_PRAD = body['recup_PRAD']
    app1 = body['app1']
    app2 = body['app2']
    reserva = body['reserva']
    restricao = body['restricao']
    area_rest = body['area_rest']

    autorizacao = get_object_or_404(Autorizacao, id=id)
    try:
        autorizacao.categoria = categoria
        autorizacao.tipo = tipo
        autorizacao.numero = numero
        autorizacao.emissao = emissao
        autorizacao.validade = validade
        autorizacao.proc_ADM = proc_ADM
        autorizacao.tcaNum = tcaNum
        autorizacao.compromitente = compromitente
        autorizacao.cpfcnpj = cpfcnpj
        autorizacao.insc_CAD = insc_CAD
        autorizacao.endereco = endereco
        autorizacao.quadra = quadra
        autorizacao.lote = lote
        autorizacao.bairro = bairro
        autorizacao.area_lote = area_lote
        autorizacao.sup_aut = sup_aut
        autorizacao.matricula = matricula
        autorizacao.anuencia_CETESB = anuencia_CETESB
        autorizacao.anuencia_CONDEMA = anuencia_CONDEMA
        autorizacao.compensacao_averbacao = compensacao_averbacao
        autorizacao.observacao = observacao
        autorizacao.objetivo = objetivo
        autorizacao.local = local
        autorizacao.nativos = nativos
        autorizacao.exoticos = exoticos
        autorizacao.euterpe = euterpe
        autorizacao.transplante = transplante
        autorizacao.vegetacao = vegetacao
        autorizacao.estagio = estagio
        autorizacao.area_aut = area_aut
        autorizacao.recup_PRAD = recup_PRAD
        autorizacao.app1 = app1
        autorizacao.app2 = app2
        autorizacao.reserva = reserva
        autorizacao.restricao = restricao
        autorizacao.area_rest = area_rest
        autorizacao.save()
        return JsonResponse({'status': '200', 'numero': numero})
    except KeyError:
        return JsonResponse({'status': '500'})


@login_required(login_url="/auth/login/")
def listar_autorizacao(request):
    if request.method == "GET":
        autorizacoes = Autorizacao.objects.all()
        return render(request, 'listar_autorizacao.html', {'autorizacoes': autorizacoes})


@login_required(login_url="/auth/login/")
def autorizacao_list(request, id):
    autorizacao = get_object_or_404(Autorizacao, id=id)
    return render(request, 'autorizacao_list.html', {'autorizacao': autorizacao})


@login_required(login_url="/auth/login/")
def baixar(request, id):
    autorizacao = get_object_or_404(Autorizacao, id=id)

    class PDF(FPDF):
        def header(self):
            # Rendering logo:
            self.image("templates/static/relatorios/imagens/cabecalho.png", 10, 8, 180)
            # Setting font: helvetica bold 15
            self.set_font("Arial", "B", 15)
            # Moving cursor to the right:
            self.cell(80)
            # Performing a line break:
            self.ln(30)

        def footer(self):
            # Position cursor at 1.5 cm from bottom:
            self.set_y(-15)
            # Setting font: helvetica italic 8
            self.set_font("Arial", "I", 8)
            # Printing page number:
            # self.cell(0, 10, f"Page {self.page_no()}", border="T", align="C")
            self.cell(0, 10, "Rua Luiz Pereira de Campos, n.º 901, Centro, Bertioga/SP | CEP 11250-117 | 13 3319.8034", border="T", align="C")

    pdf = PDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.set_fill_color(240, 240, 240)

    pdf.cell(80, 10, 'AUTORIZACAO AMBIENTAL', 0, 0, 'C')  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(30, 10, 'Categoria', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, 'Tipo', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, 'Número', 0, 1, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501

    pdf.cell(80, 10, '', 0, 0)
    pdf.cell(30, 10, f'{autorizacao.categoria}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, f'{autorizacao.tipo}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, f'{autorizacao.numero}', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(30, 10, 'Emissão', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, 'Validade', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(70, 10, 'Processo Administrativo', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, 'TCA nº', 0, 1, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501

    pdf.cell(30, 10, f'{autorizacao.emissao}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, f'{autorizacao.validade}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(70, 10, f'{autorizacao.proc_ADM}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, f'{autorizacao.tcaNum}', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(100, 10, 'Compromitente', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, 'CPF / CNPJ', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(40, 10, 'Inscrição Cadastral', 0, 1, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501

    pdf.cell(100, 10, f'{autorizacao.compromitente}', 1, 0, 'L', 10)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(30, 10, f'{autorizacao.cpfcnpj}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(40, 10, f'{autorizacao.insc_CAD}', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(100, 10, 'Endereço do Imóvel', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(15, 10, 'Quadra', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(15, 10, 'Lote', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(40, 10, 'Bairro', 0, 1, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501

    pdf.cell(100, 10, f'{autorizacao.endereco}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(15, 10, f'{autorizacao.quadra}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(15, 10, f'{autorizacao.lote}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(40, 10, f'{autorizacao.bairro}', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(30, 10, 'Área do Lote', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(45, 10, 'Supressão Autorizada', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(90, 10, 'Matrícula do Imóvel - CRI', 0, 1, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501

    pdf.cell(30, 10, f'{autorizacao.area_lote}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(45, 10, f'{autorizacao.sup_aut}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(90, 10, f'{autorizacao.matricula}', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(40, 10, 'Anuência CETESB', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(45, 10, 'Anuência CONDEMA', 0, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(90, 10, 'Compensação / Averbação', 0, 1, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501

    pdf.cell(40, 10, f'{autorizacao.anuencia_CETESB}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(45, 10, f'{autorizacao.anuencia_CONDEMA}', 1, 0, 'L', 0)
    pdf.cell(5, 10, '', 0, 0)
    pdf.cell(90, 10, f'{autorizacao.compensacao_averbacao}', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(30, 10, 'Observações', 0, 0, 'L', 1)
    pdf.cell(150, 10, f'{autorizacao.observacao}', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(190, 10, 'Árvores Isoladas', 0, 1, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501

    pdf.cell(50, 10, 'Objetivo', 0, 0)
    pdf.cell(50, 10, 'Local', 0, 0)
    pdf.cell(90, 10, 'Quantidade autorizada', 0, 1)

    pdf.cell(45, 10, f'{autorizacao.objetivo}', 1, 0, 'L', 0)
    pdf.cell(45, 10, f'{autorizacao.local}', 1, 0, 'L', 0)
    pdf.cell(33, 10, f'{autorizacao.nativos} nativos', 1, 0, 'L', 0)
    pdf.cell(33, 10, f'{autorizacao.exoticos} exoticos', 1, 0, 'L', 0)
    pdf.cell(33, 10, f'{autorizacao.euterpe} euterpe edulis', 1, 1, 'L', 0)
    pdf.ln(5)

    pdf.cell(190, 10, 'CONSIDERAÇÕES:', 0, 1, 'L', 0)
    pdf.cell(190, 10, '1. Esta AUTORIZAÇÃO está em conformidade com o disposto na Lei Complementar n.º 140/2011', 0, 1, 'L', 0)
    pdf.cell(190, 10, '2. A Autorização Ambiental Municipal não exime da necessidade de outras autorizações', 0, 1, 'L', 0)

    pdf_content = pdf.output(dest='S').encode('latin1')  # Salvar o pdf em memória
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os_{autorizacao.id}.pdf")
