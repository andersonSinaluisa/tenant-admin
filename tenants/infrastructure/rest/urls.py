from rest_framework.routers import DefaultRouter
from tenants.infrastructure.rest.views.tenant_view import TenantViewSet
from tenants.infrastructure.rest.views.plan_view import PlanViewSet


router = DefaultRouter()
router.register(r'tenants', TenantViewSet, basename='tenant')
router.register(r'planes', PlanViewSet, basename='plan')

urlpatterns = router.urls
