from django.contrib import admin
from django.urls import path, include
from core.views import home

# necessary importing for media files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homepage'),

    path('member/', include('member.urls')),
    path('transaction/', include('transaction.urls')),

    path('book/', include('book.urls')),
    path('category/', include('category.urls')),
    
    path('categories/<slug:category_slug>/', home, name='category_wise_book'),

    path('activity/', include('activity.urls')),
]

# adding media url to urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

