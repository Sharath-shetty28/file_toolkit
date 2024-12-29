from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfMerger

def merge_pdfs(request):
    if request.method == "POST":
        files = request.FILES.getlist('pdfs')
        if not files:
            return HttpResponse("No files uploaded.", status=400)

        merger = PdfMerger()
        first_file_name = files[0].name.split('.')[0]  # Extract the name of the first file (without extension)

        for file in files:
            merger.append(file)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{first_file_name}_merged.pdf"'
        merger.write(response)
        merger.close()

        return response

    return render(request, 'merge_pdfs.html')

def index(request):
    return render(request, 'index.html')

