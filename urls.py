from django.conf.urls import patterns, url

from ukbooking import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^booking/(?P<booking_id>\d+)/$', views.booking, name='booking'),
                       url(r'^bookings/(?P<year>\d+)/(?P<month>\d+)/$', views.bookings, name='bookings'),
                       url(r'^bookings/dump/$', views.Bookings.as_view(), name='bookings_dump'),
                       url(r'^bookings/$', views.bookings, name='bookings'),


                       url(r'^book_visit/$', views.book_visit, name='book_visit'),

                       url(r'^visit/(?P<visit_id>\d+)/$', views.visit, name='visit'),
                       url(r'^visits/(?P<year>\d+)/(?P<month>\d+)/$', views.visits, name='visits'),
                       url(r'^visits/dump/$', views.Visits.as_view(), name='visits_dump'),
                       url(r'^visits/$', views.visits, name='visits'),

                       url(r'^apartments/$', views.Apartments.as_view(), name='apartments'),
                       url(r'^apartment/(?P<apartment_id>\d+)/$', views.apartment, name='apartment'),
)
