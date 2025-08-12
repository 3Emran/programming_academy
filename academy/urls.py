# academy/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # or your homepage
    path('blog/', include('blog.urls')),
    path('quiz/', include('quiz.urls')),  # ✅ This must be here
]

# Static and media files (important for deployment)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    

# Dummy views for now
def placeholder_view(request):
    return HttpResponse("This page is under construction.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),             # Home page from the courses app
    path('about/', placeholder_view, name='about'),
    path('faq/', placeholder_view, name='faq'),
    path('contact/', placeholder_view, name='contact'),
    path('blog/', placeholder_view, name='blog'),
    path('team/', placeholder_view, name='team'),
    path('events/', placeholder_view, name='events'),
    path('newsletter/', placeholder_view, name='newsletter'),
    path('testimonial/', placeholder_view, name='testimonial'),
    path('login/', placeholder_view, name='login'),
    path('signup/', placeholder_view, name='signup'),
]
