from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',

        url(r'^$', IndexView.as_view(), name='index'),
        url(r'^add-book/$', BookCreateView.as_view(), name='book_create'),
        url(r'^edit-book/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='book_edit'),

        url(r'^login/$', user_login, name='login'),
        url(r'^logout/$', user_logout, name='logout'),

        url(r'^user/$', user_test, name='user_test'),
        url(r'^requests/$',RequestsView.as_view(), name='requests'),
        url(r'^logs/$', logs, name='logs'),
)