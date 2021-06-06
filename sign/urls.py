# project\sign\urls.py 路徑下的程式碼。
from django.urls import path
from . import views
#每一個網頁的子層要寫於此
urlpatterns = [
    path('', views.index, name='index'),
    path('general_catalog/', views.general_catalog, name='general_catalog'),
    path('general_catalog/catalog/', views.catalog, name='catalog'),
    path('general_catalog/catalog/exercise/', views.exercise, name='exercise'),
    path('answers/', views.answers, name='answers'),
    path('answers/<int:answer_id>/', views.answer_detail, name='answer_detail'),
]