# coding=utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from citasalud.apps.api.viewsets import MedicoViewSet, EspecialidadViewSet, UsuarioViewSet, EmpleadoViewSet

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from citasalud.apps.api.views import CurrentUserView

admin.autodiscover()

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'empleados', EmpleadoViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'citasalud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/usuario/', CurrentUserView.as_view() ),
    url(r'^api/auth/token/', views.obtain_auth_token),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)