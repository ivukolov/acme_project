from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('birthday/', include('birthday.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
