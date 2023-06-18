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
            name_origin = uploadfile.name  # 원본 파일
            fs = FileSystemStorage(location='static/source')  #서버에 저장된 파일
            imgname = fs.save(f'src-{name_origin}', uploadfile)

            imgfile = Image.open(f'static/source/{imgname}') #파일 열기
            result_text = pytesseract.image_to_string(imgfile, lang='kor+eng') #문자로 변환
            result_text = result_text.replace(" ", "")
    context = {
        'imgname': imgname,
        'result_text': result_text
    }
    return render(request, 'ocr/ocr_upload.html', context)
