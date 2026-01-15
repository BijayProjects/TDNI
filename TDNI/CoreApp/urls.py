from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Contact Form Submission
    path('contact/submit/', views.submit_contact, name='submit_contact'),

    # Client Review Submission
    path('review/submit/', views.submit_review, name='submit_review'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)