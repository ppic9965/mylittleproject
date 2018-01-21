from django.conf.urls import url
from django.contrib import admin
from download import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.download),
    url(r'^down/$', views.pdf_download, name='down')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

