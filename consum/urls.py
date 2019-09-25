from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.contrib.auth.views import logout

urlpatterns = [
    url('', views.home, name='home'),
    url('', include('social_django.urls', namespace='social')),
    url('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),
    
]