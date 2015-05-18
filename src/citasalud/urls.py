from django.conf.urls import include, url
from django.contrib import admin
from citasalud.apps.api.viewsets import MedicoViewSet, EspecialidadViewSet, UsuarioViewSet

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from citasalud.apps.api.views import CurrentUserView

admin.autodiscover()

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'usuarios', UsuarioViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'citasalud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/currentuser', CurrentUserView.as_view() ),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth-token/', views.obtain_auth_token),
    url(r'^admin/', include(admin.site.urls)),
]
