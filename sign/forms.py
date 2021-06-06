from django import forms
#from .models import Charpter1Model

class Chapter1Form(forms.Form):
    chapter1 = (
       ('1-1','1'),  
       ('1-2','2'),
       ('1-3','3'),
       ('1-4','4'),
       ('1-5','5'),
       ('1-6','6'),
    )  #前面是展示在前端界面的内容,后面的'1'是真正存在数据库中的
    chapter1_value=forms.CharField(max_length=10,widget=forms.widgets.Select(choices=chapter1))

