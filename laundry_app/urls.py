from django.conf.urls import patterns, url, include

urlpatterns = patterns('laundry_app.views',
    url(r'^ajax/current/(?P<hall>\d+)/$', 'ajax_get_current', name='get_current_chart'),
    url(r'^$', 'main_page', name='laundry_main'),
)
