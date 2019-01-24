"""simplesocial URL Configuration"""


from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.HomeView.as_view() , name='home'),
    path('accounts/', include('accounts.urls' , namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/' , views.TestPage.as_view() , name='test'),
    path('thanks/' , views.ThnaksPage.as_view() , name='thanks'),
    path('posts/', include('posts.urls' , namespace='posts')),
    path('groups/', include('groups.urls' , namespace='groups')),

]



# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
