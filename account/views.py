import mimetypes
from django.http.response import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import UploadedFile
# from .forms import UploadFileForm
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('upload_file')
#     else:
#         form = UploadFileForm()
#     files = UploadedFile.objects.all()
#     return render(request, 'index.html', {'form': form, 'files': files})
#
# def download_file(request, file_id):
#     uploaded_file = UploadedFile.objects.get(pk=file_id)
#     response = HttpResponse(uploaded_file.file, content_type='application/force-download')
#     response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
#     return response


# def download_file(request):
#     # Define Django project base directory
#     BASE_DIR = "/home/diyorbek/PycharmProjects/Modul7/Resumue"
#     # Define text file name
#     filename = 'resume.pdf'
#     # Define the full file path
#     filepath = BASE_DIR + '/account/media/' + filename
#     # Open the file for reading content
#     path = open(filepath, 'r')
#     # Set the mime type
#     mime_type, _ = mimetypes.guess_type(filepath)
#     # Set the return value of the HttpResponse
#     response = HttpResponse(path, content_type=mime_type)
#     # Set the HTTP header for sending to browser
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     # Return the response value
#     return response


#
# def download_cv(request):
#     # 'media' papkasi ichidagi 'resume.pdf' faylini tanlang
#     file_path = os.path.join(settings.MEDIA_ROOT, 'resume.pdf')
#     # 'resume.pdf' faylini foydalanuvchiga yuborish
#     with open(file_path, 'rb') as pdf_file:
#         response = FileResponse(pdf_file, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
#     return response
