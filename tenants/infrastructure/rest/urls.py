from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tenants.infrastructure.rest.views.tenant_view import TenantViewSet
from tenants.infrastructure.rest.views.plan_view import PlanViewSet
from tenants.infrastructure.rest.views.contact_view import ContactoViewSet
from tenants.infrastructure.rest.views.configuracion_view import ConfiguracionViewSet
from tenants.infrastructure.rest.views.licencia_view import LicenciaViewSet
from tenants.infrastructure.rest.views.modulo_view import ModuloViewSet
from tenants.infrastructure.rest.views.logo_view import LogoViewSet
from tenants.infrastructure.rest.views.almacenamiento_view import AlmacenamientoViewSet
from tenants.infrastructure.rest.views.auditoria_view import AuditoriaViewSet



router = DefaultRouter()
router.register(r'tenants', TenantViewSet, basename='tenant')
router.register(r'planes', PlanViewSet, basename='plan')

urlpatterns = [
    path('', include(router.urls)),
    path('tenants/<uuid:tenant_id>/contactos/',
         ContactoViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='tenant-contactos'),
    path('tenants/<uuid:tenant_id>/contactos/<uuid:pk>/',
         ContactoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='tenant-contactos-detail'),
    path('tenants/<uuid:tenant_id>/configuracion/',
         ConfiguracionViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='tenant-configuracion'),
    path('tenants/<uuid:tenant_id>/configuracion/bulk-update/',
         ConfiguracionViewSet.as_view({'post': 'bulk_update'}),
         name='tenant-configuracion-bulk'),
    path('tenants/<uuid:tenant_id>/configuracion/<uuid:pk>/',
         ConfiguracionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='tenant-configuracion-detail'),
    path('tenants/<uuid:tenant_id>/licencias/',
         LicenciaViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='tenant-licencias'),
    path('tenants/<uuid:tenant_id>/licencias/<uuid:pk>/',
         LicenciaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='tenant-licencias-detail'),
    path('tenants/<uuid:tenant_id>/licencias/<uuid:pk>/renew/',
         LicenciaViewSet.as_view({'post': 'renew'}),
         name='tenant-licencias-renew'),
    path('tenants/<uuid:tenant_id>/modulos/',
         ModuloViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='tenant-modulos'),
    path('tenants/<uuid:tenant_id>/modulos/<uuid:pk>/',
         ModuloViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='tenant-modulos-detail'),
    path('tenants/<uuid:tenant_id>/modulos/<uuid:pk>/enable/',
         ModuloViewSet.as_view({'post': 'enable'}),
         name='tenant-modulos-enable'),
    path('tenants/<uuid:tenant_id>/modulos/<uuid:pk>/disable/',
         ModuloViewSet.as_view({'post': 'disable'}),
         name='tenant-modulos-disable'),
    path('tenants/<uuid:tenant_id>/branding/',
         LogoViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}),
         name='tenant-branding'),
    path('tenants/<uuid:tenant_id>/almacenamiento/',
         AlmacenamientoViewSet.as_view({'get': 'list'}),
         name='tenant-almacenamiento'),
    path('tenants/<uuid:tenant_id>/almacenamiento/actualizar/',
         AlmacenamientoViewSet.as_view({'post': 'actualizar'}),
         name='tenant-almacenamiento-actualizar'),
    path('tenants/<uuid:tenant_id>/auditoria/',
         AuditoriaViewSet.as_view({'get': 'list'}),
         name='tenant-auditoria'),
    path('tenants/<uuid:tenant_id>/auditoria/<uuid:pk>/',
         AuditoriaViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}),
         name='tenant-auditoria-detail'),
]


