from django.shortcuts import render
from .forms import Chapter1Form
from .models import Answer, Question

# Create your views here.


def index(request):
    return render(request, "index.html")  # 將index.html頁面拋給使用者


def general_catalog(request):

    if "chapter" in request.GET:  # 若搜尋表單接受到值
        name = (  # request.GET是字典，name會儲存?-? ?.
            request.GET.get("chapter")
            + "-"
            + request.GET.get("part")
            + " "
            + request.GET.get("exercises number")
            + "."
        )
        answer = Answer.objects.get(title=name)  # 令answer為模型Answer裡title為?-? ?.的那筆資料
        question = Question.objects.get(
            title=name
        )  # 令question為模型Question裡title為?-? ?.的那筆資料
        return render(
            request,
            "exercise.html",
            {"answer": answer, "question": question},  # 給題目頁面，並將answer與question變數傳進去該頁面
        )
    if "chapter1" in request.GET:  # 若下拉式表單收到值
        name = "1-" + str(request.GET.get("chapter1"))  # 令name為1-?
        Chapterlist = [
            Chapterlist for Chapterlist in Answer.objects.filter(title__contains=name)
        ]  # Chapterlist 是一個list裡面有所有title含1-?的每筆資料(取得所有該節的每筆題目+答案)

        return render(
            request, "catalog.html", {"Chapterlist": Chapterlist, "name": name}
        )  # 給單節目錄網頁，並將name及Chapterlist傳進去
    else:
        return render(
            request, "general_catalog.html", {"chapter1_form": Chapter1Form}
        )  # 給出總目錄的網頁並把 Chapter1Form這個表單給總目錄網頁


def catalog(request):
    answers = Answer.objects.all()
    return render(request, "catalog.html", {"answers": answers})


def exercise(request, ans_id):
    answer = Answer.objects.get(id=ans_id)  # 取得id為使用者要求之數的該筆資料
    question = Question.objects.get(
        title=answer.title
    )  # answer.title取得模型Answer中該id的那筆資料的標題(?-? ?.)
    if "chapter" in request.GET:  # 同總目錄搜尋表單運作
        name = (
            request.GET.get("chapter")
            + "-"
            + request.GET.get("part")
            + " "
            + request.GET.get("exercises number")
            + "."
        )
        answer = Answer.objects.get(title=name)
        question = Question.objects.get(title=name)
        return render(
            request,
            "exercise.html",
            {"answer": answer, "question": question},
        )
    else:
        return render(
            request,
            "exercise.html",
            {"answer": answer, "question": question},  # 給題目頁面，並將answer與question變數傳進去該頁面
        )
