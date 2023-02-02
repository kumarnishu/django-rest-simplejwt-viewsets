from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("", include("api.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
