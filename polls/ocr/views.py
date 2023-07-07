import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from PIL import Image
from pytesseract import pytesseract

# tesseract 실행 환경
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def ocr_read(request):
    imgname = ''      #이미지 파일
    result_text = ''  #변환된 결과 텍스트
    if 'uploadfile' in request.FILES:  #파일중에 업로드 파일이 있다면
        uploadfile = request.FILES.get('uploadfile') # 업로드 파일 1개 가져옴

        name_origin = uploadfile.name  # 원본 파일
        fs = FileSystemStorage(location='static/source')  # 서버의 저장 파일 경로
        imgname = fs.save(f'src-{name_origin}', uploadfile)  # 파일 저장

        imgfile = Image.open(f'static/source/{imgname}') #저장 경로에서 파일 열기
        result_text = pytesseract.image_to_string(imgfile, lang='kor+eng') #문자로 변환
        result_text = result_text.replace(" ", "")
    context = {
        'imgname': imgname,
        'result_text': result_text
    }
    return render(request, 'ocr/ocr_read.html', context)
