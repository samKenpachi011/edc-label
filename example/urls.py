from django.conf.urls import url, include
from django.contrib import admin

from edc_base.views.login_view import LoginView
from edc_base.views.logout_view import LogoutView
from django.views.generic.base import RedirectView

from .views import HomeView

urlpatterns = [
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(pattern_name='login_url'), name='logout_url'),
    # url(r'^call_manager/$', RedirectView.as_view(pattern_name='home_url')),
    url(r'^edc_label/', include('edc_label.urls', namespace='edc-label')),
    url(r'^edc/', include('edc_base.urls', 'edc-base')),
    url(r'^admin/$', RedirectView.as_view(pattern_name='home_url')),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', HomeView.as_view(), name='home_url'),
    url(r'^', HomeView.as_view(), name='home_url'),
]
