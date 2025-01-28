from django.urls import path, include
from rest_framework import routers

from book.views import BookView

router = routers.DefaultRouter()
router.register('api', BookView)

urlpatterns = [
    path('', include(router.urls)),
]