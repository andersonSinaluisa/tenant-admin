from django.http import JsonResponse
from .models import Tenant


def list_tenants(request):
    data = list(Tenant.objects.values('id', 'nombre', 'dominio', 'estado'))
    return JsonResponse(data, safe=False)
