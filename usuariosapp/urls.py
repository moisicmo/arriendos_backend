from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from usuariosapp.views import TaskViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

class Task(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"content": "Esta vista está protegida"})

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('token/', TokenObtainPairView.as_view(), name='token_obten_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]