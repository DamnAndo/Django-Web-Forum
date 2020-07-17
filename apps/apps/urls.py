from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path("forum/",include("forum.urls")),
    path("",TemplateView.as_view(template_name="welcome.html"),name="home"),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
