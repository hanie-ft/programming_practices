from django.urls import path, include

urlpatterns = [
    path('blog/', include(('sampletemplateproject.blog.urls', 'blog')))
]
