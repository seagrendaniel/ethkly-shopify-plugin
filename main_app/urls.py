from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', include('shopify_auth.urls')),
    path('shopify', views.install, name="install"),
    # ... remaining configuration here ...
]