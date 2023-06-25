from django import forms

# 클라이언트 화면에 입력 폼을 만듬
# 클라이언트가 입력한 데이터에 대한 전처리(유효성 검사)

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()  #수량
    is_update = forms.BooleanField(required=False,
                initial=False, widget=forms.HiddenInput)
    #hiddenInput - 사용자는 알지 못함