from django.urls import include, path
from .views import hello , status , colado
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
    path('', include(router.urls)),
] 