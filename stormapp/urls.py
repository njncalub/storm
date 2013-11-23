from django.conf.urls.defaults import patterns, include, url
from stormapp.deadbodies.views import home_view, sample_map_view, report_dead_body, view_all_dead_body

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
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
)