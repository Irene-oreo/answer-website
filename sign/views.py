from django.shortcuts import render
from .forms import Chapter1Form
from .models import Chapter, lists, Answer
# Create your views here.


class Chapterlist():
    chapter1_1_list = (('1.', 'yes'), ('2.', 'no'))
    chapter1_2_list = (('1.', 'yes'), ('2.', 'no'))
    chapter1_3_list = (('1.', 'yes'), ('2.', 'no'))


a = '1'


def index(request):
    return render(request, "index.html")  # 將index.html頁面拋給使用者


def general_catalog(request):

    if 'chapter' in request.GET:  # request.GET是字典，會儲存對應的輸入name與其值
        chapter = request.GET.get('chapter')
        part = request.GET.get('part')
        exercises_number = request.GET.get('exercises number')
        return render(request, "exercise.html", {'chapter': chapter, 'part': part, 'exercises_number': exercises_number})
    if 'chapter1' in request.GET:
        global a
        a = '1-'+str(request.GET.get('chapter1'))
        Chapter.objects.create(title=a)

        return render(request, "catalog.html", {'Chapterlist': Chapterlist(), 'name': a})
    else:
        return render(request, "general_catalog.html", {'chapter1_form': Chapter1Form})


def catalog(request):
    catalog_list = lists.objects.all()
    return render(request, "catalog.html", {'catalog_list': catalog_list})


def exercise(request):
    global a
    b = Chapter.objects.get(title=a)
    print(b.title)
    if 'chapter' in request.GET:  # request.GET是字典，會儲存對應的輸入name與其值
        chapter = request.GET.get('chapter')
        part = request.GET.get('part')
        exercises_number = request.GET.get('exercises number')
        return render(request, "exercise.html", {'chapter': chapter, 'part': part, 'exercises_number': exercises_number})
    else:
        return render(request, "exercise.html", {'name': b.title})

def answers(request):
    answers = Answer.objects.all()
    return render(request, 'answer_list.html', {'answers': answers})

def answer_detail(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    return render(request, 'answer_detail.html', {'answer': answer})
