from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'prefetch_vs_related.views.home', name='home'),
    # url(r'^prefetch_vs_related/', include('prefetch_vs_related.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT,
         'show_indexes': True}),

    url(r'^$', 'talk_example.views.home'),
    url(r'^prefetch/', 'talk_example.views.prefetch'),
    url(r'^select/', 'talk_example.views.select'),
)

urlpatterns += staticfiles_urlpatterns()
