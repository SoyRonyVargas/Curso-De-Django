from django.urls import include, path
from .views import hello , status , colado , detalleProducto
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'products',
    ProductViewSet,
    basename='product'
)

# urlpatterns = router.urls

urlpatterns = [
    path('hello/', hello),
    path('status/', status),
    path('colado/', colado),
    path('producto/', detalleProducto),
    path('', include(router.urls)),
] 