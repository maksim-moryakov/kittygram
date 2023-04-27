from django.urls import include, path
from rest_framework.routers import SimpleRouter
from cats.views import cat_list, CatViewSet

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)

# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
   path('cats/', cat_list, name='cat_list'),
   path('cat/<int:pk>/', ..., name='cat-detail'),
   path('', include(router.urls)),
]



