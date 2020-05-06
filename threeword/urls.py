
from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('gocreate', views.go_create, name="go_create"),

    path('posts/<int:pk>/', views.translate, name="translate"),

    path('create', views.create_post, name="create"),
    path('readbylike', views.read_posts_by_like, name="readbylike"),
    path('readbydate', views.read_posts_by_date, name="readbydate"),
    path('heart/<int:pk>', views.raise_heart, name="heart"),


    path('rank', views.rank, name="rank"),
    path('list', views.list, name="list"),
    path('update_bool/<int:pk>/', views.update_bool, name="update_bool"),

    path('other_prompt/<int:pk>', views.other_prompt, name="other_prompt")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
