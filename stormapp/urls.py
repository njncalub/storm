from django.conf.urls.defaults import patterns, include, url
from stormapp.deadbodies.views import report_dead_body, view_all_dead_body

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# deadbodies
urlpatterns += patterns('',
    url(r'^report/$', report_dead_body),
    url(r'^view_all/$', view_all_dead_body),
)