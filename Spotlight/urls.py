from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'Spotlight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html'),name='home'),
	url(r'^spotlight/', include('spotlightapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
