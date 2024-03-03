from rest_framework import routers
from django.urls import path,include
from mau import views

router = routers.DefaultRouter()
router.register(r"gato", views.GatosView , "gato")

urlpatterns=[

    path("api/1/", include(router.urls))
]