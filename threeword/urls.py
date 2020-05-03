
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('gocreate', views.go_create, name="go_create"),
    # path('postread/<int:pk>', views.main_read, name="mainread"),
    path('create', views.create_post, name="create"),
    path('readbylike', views.read_posts_by_like, name="readbylike"),
    path('readbydate', views.read_posts_by_date, name="readbydate"),
    path('heart/<int:pk>', views.raise_heart, name="heart"),

]
