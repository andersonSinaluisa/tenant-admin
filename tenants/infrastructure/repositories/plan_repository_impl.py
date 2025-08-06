from tenants.domain.repositories.plan_repository import PlanRepository
from tenants.infrastructure.persistence.plan_django_model import TenantPlan


class DjangoPlanRepository(PlanRepository):
    def list(self):
        return TenantPlan.objects.all()

    def retrieve(self, plan_id):
        return TenantPlan.objects.get(id=plan_id)
