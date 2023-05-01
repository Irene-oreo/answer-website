# project\sign\urls.py 路徑下的程式碼。
from django.urls import path
from . import views

# 每一個網頁的子層要寫於此
urlpatterns = [
    path("", views.index, name="index"),  # https://...../   是首頁，會呼叫views裡的index函式
    path(
        "general_catalog/", views.general_catalog, name="general_catalog"
    ),  # https://...../general_catalog/  是總目錄，，會呼叫views裡的general_catalog函式
    path(
        "general_catalog/catalog/", views.catalog, name="catalog"
    ),  # https://...../general_catalog/catalog  是單節目錄，，會呼叫views裡的catalog函式
    path(
        "general_catalog/catalog/exercise/<int:ans_id>/",
        views.exercise,
        name="exercise",
    ),  # https://...../general_catalog/catalog/exercise/<int:ans_id>/  是題目頁面，會呼叫views裡的exercise函式`,<int:ans_id>代表那裡預期會接收到一個int，其變數名為ans_id
]
