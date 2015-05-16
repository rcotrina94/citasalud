from django.conf.urls import include, url
from django.contrib import admin
from citasalud.apps.api.viewsets import MedicoViewSet, EspecialidadViewSet

from rest_framework.routers import DefaultRouter


admin.autodiscover()

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)
router.register(r'especialidades', EspecialidadViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'citasalud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
