from django.urls import include, path

urlpatterns = [
    path('login/', include('shopify_auth.urls')),

    # ... remaining configuration here ...
]