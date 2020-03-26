
from django.contrib import admin
from django.urls import path
from webroot import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name = "signup"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('', views.home, name = "home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
