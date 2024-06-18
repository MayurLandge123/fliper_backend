from django.urls import path
from .views import RoleCreateView

urlpatterns = [
    path('v1/role', RoleCreateView.as_view(), name='create-role'),
]
