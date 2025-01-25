import json
import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

class Middleware(MiddlewareMixin):
    def process_request(self, request):
        # Obtener el token de autorización del encabezado
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.replace("Bearer ", "")
            
            # Crear el cuerpo de la solicitud para la verificación de permisos
            permission_data = {
                "url": request.path,
                "method": request.method
            }
            
            try:
                print("hola si llegue")
                # Llamar al microservicio de seguridad
                response = requests.post(
                    f"{settings.MS_SECURITY}/api/public/security/permissions-validation",
                    json=permission_data,
                    headers={
                        "Authorization": f"Bearer {token}"
                    },
                    timeout=10  # Establecer un tiempo de espera para evitar bloqueos
                )
                print(response.json)
                
                # Verificar la respuesta del microservicio
                if response.status_code == 200 and response.json() is True:
                    logger.info("Permiso concedido por el microservicio de seguridad.")
                    return None  # Continuar con el flujo de la solicitud
                
                logger.warning("Acceso denegado por el microservicio de seguridad.")
                return JsonResponse({"detail": "Unauthorized access. 1"}, status=401)
            
            except requests.RequestException as e:
                logger.error(f"Error al comunicarse con el microservicio de seguridad: {e}")
                return JsonResponse({"detail": "Unauthorized access.2"}, status=401)
        else:
            logger.warning("No se proporcionó un token de autorización.")
            return JsonResponse({"detail": "Unauthorized access. 3"}, status=401)
