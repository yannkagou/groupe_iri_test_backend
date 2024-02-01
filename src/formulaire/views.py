import pdfkit

from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template

from .models import Formulaire
from .serializers import FormulaireSerializer

class FormulaireViewSet(viewsets.ModelViewSet):
    serializer_class = FormulaireSerializer
    queryset = Formulaire.objects.all()


def generate_pdf(request, formulaire_id):
    formulaire = get_object_or_404(Formulaire, pk=formulaire_id)

    template_name = 'pdf.html'
    template = get_template(template_name)
    html = template.render({'formulaire': formulaire})

    options = {
        'encoding': 'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options=options)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="formulaire.pdf"'
    response.write(pdf)

    return response
