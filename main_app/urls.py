from . import views
from django.urls import include, path

urlpatterns = [
    # path('', views.home, name="home"),
    path('login/', include('shopify_auth.urls')),
    path('', views.install, name="install"),
    path('connect/', views.connect, name="connect")
    # ... remaining configuration here ...

]

