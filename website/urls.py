from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^login/$', views.login),
	]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)