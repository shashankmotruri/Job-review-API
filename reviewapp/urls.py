from django.urls import path
from . import views
from drf_yasg import openapi 
from drf_yasg.views import get_schema_view as swagger_get_schem_view

schema_view = swagger_get_schem_view(
    openapi.Info(
        title = "All APIs",
        default_version = '3.0.0',
        description = "API Documentation",
    )

)

urlpatterns = [
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0)),
    path('',views.CandidateListCreateView.as_view(),name='list-create'),
    path('<int:pk>',views.CandidateUpdateDeleteView.as_view(),name='update-delete'),
]