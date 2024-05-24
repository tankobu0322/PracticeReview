from django.contrib import admin
from django.urls import path
from review.views import index,upload_chorus,upload_success,watch_review

urlpatterns = [
    path('', index, name='index'),
    path('upload/',upload_chorus,name='upload'),
    path('upload_success/',upload_success,name='soushin'),
    path('watchreview/',watch_review,name='watchreview'),
    path('admin/', admin.site.urls),
]
