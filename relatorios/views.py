from django.shortcuts import render, get_object_or_404
from .forms import FormRelatorio
from django.http import HttpResponse, FileResponse
from .models import Relatorio
from fpdf import FPDF
from io import BytesIO
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login/")
def novo_relatorio(request):
    if request.method == "GET":
        form = FormRelatorio()
        return render(request, 'novo_relatorio.html', {'form': form})
    elif request.method == "POST":
        form = FormRelatorio(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Salvo com Sucesso")
        else:
            return render(request, 'novo_relatorio.html', {'form': form})


@login_required(login_url="/auth/login/")
def listar_relatorio(request):
    if request.method == "GET":
        relatorios = Relatorio.objects.all()
        return render(request, 'listar_relatorio.html', {'relatorios': relatorios})


@login_required(login_url="/auth/login/")
def relatorio(request, identificador):
    relatorio = get_object_or_404(Relatorio, identificador=identificador)
    return render(request, 'relatorio.html', {'relatorio': relatorio})


@login_required(login_url="/auth/login/")
def baixar_os(request, identificador):
    relatorio = get_object_or_404(Relatorio, identificador=identificador)

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
            self.cell(0, 10, f"Page {self.page_no()}", align="C")

    pdf = PDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.set_fill_color(240, 240, 240)
    pdf.cell(35, 10, 'Título:', 1, 0, 'L', 1)  # altura, largura, nome, borda, passar para a próxima linha, alinhamento, cor de fundo  # noqa: E501
    pdf.cell(0, 10, f'{relatorio.titulo}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Relatórios:', 1, 0, 'L', 1)
    categorias_relatorio = relatorio.categoria_relatorio.all()
    for i, relatoriox in enumerate(categorias_relatorio):
        pdf.cell(0, 10, f' - {relatoriox.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(categorias_relatorio) - 1:
            pdf.cell(35, 10, '', 0, 0)

    pdf.cell(35, 10, 'Data Geração:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{relatorio.data_geracao}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{relatorio.protocolo}', 1, 1, 'L', 1)

    pdf_content = pdf.output(dest='S').encode('latin1')  # Salvar o pdf em memória
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os_{relatorio.titulo}.pdf")


@login_required(login_url="/auth/login/")
def relatorio_inicio(request):
    return render(request, 'relatorio_inicio.html')
