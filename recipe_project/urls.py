from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('recipe_app.urls')),  # Include the URLs from your app
    # Add any other top-level URL patterns if needed
]
