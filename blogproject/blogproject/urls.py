from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #html form을 이용해서 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    #127.0.0.1:8000/detail/primarykey
    #127.0.0.1:8000/detail/1
    #127.0.0.1:8000/detail/2
    #127.0.0.1:8000/detail/3

    path('detail/<int:blog_id>', views.detail, name='detail'),


    path('create_comment/<int:blog_id>',views.create_comment, name='create_comment'),


    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # mediafile에 접근할 수 있는 url도 추가하여야 한다.
    # 그냥 외워 위에 import 하는 과정도 외워
