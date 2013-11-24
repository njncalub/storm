from django.conf.urls.defaults import patterns, include, url
from django.http import HttpResponseRedirect
from stormapp.deadbodies.views import home_view, sample_map_view, retrieve_body, report_dead_body, view_all_dead_body
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# deadbodies
urlpatterns += patterns('',
    url(r'^index/$', home_view),
    url(r'^view_map/$', sample_map_view),
    url(r'^report/$', report_dead_body),
    url(r'^view_all/$', view_all_dead_body),
    url(r'^retrieve/$', view_all_dead_body),
    url(r'^$', lambda x: HttpResponseRedirect('/index/')),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )