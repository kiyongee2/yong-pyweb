import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from PIL import Image
from pytesseract import pytesseract

# tesseract 실행 환경
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def ocr_upload(request):
    imgname = ''
    result_text = ''
    if 'uploadfile' in request.FILES:
        uploadfile = request.FILES.get('uploadfile')

        if uploadfile != '':
            name_old = uploadfile.name
            name_ext = os.path.splitext(name_old)[1]

            fs = FileSystemStorage(location='static/source')
            imgname = fs.save(f'src-{name_old}', uploadfile)

            imgfile = Image.open(f'static/source/{imgname}')
            result_text = pytesseract.image_to_string(imgfile, lang='kor+eng')
            result_text = result_text.replace(" ", "")

    context = {
        'imgname': imgname,
        'result_text': result_text
    }
    return render(request, 'ocr/ocr_upload.html', context)
