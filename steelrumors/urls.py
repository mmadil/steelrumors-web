# -*- coding: utf-8 -*-
"""Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
"""
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as dj_default_views
from django.views.generic import TemplateView
from registration.backends.simple.views import RegistrationView
# steelrumors Stuff
from steelrumors.base import views as base_views
from steelrumors.links.views import LinkListView, LinkDetailView, LinkCreateView, LinkUpdateView, LinkDeleteView
from steelrumors.links.views import VoteFormView
from steelrumors.users.forms import CustomUserRegistrationForm
from steelrumors.users.views import UserProfileDetailView, UserProfileUpdateView
from .routers import router

handler500 = base_views.server_error

# Top Level Pages
# ==============================================================================
urlpatterns = [
    url(r'^$', LinkListView.as_view(), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # accounts
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=CustomUserRegistrationForm), name='register'),
    url(r'^accounts/profile/(?P<username>\w+)/$', UserProfileDetailView.as_view(), name='profile'),
    url(r'^accounts/edit/$', UserProfileUpdateView.as_view(), name='edit_profile'),

    # links
    url(r'^link/create/$', LinkCreateView.as_view(), name='link_create'),
    url(r'^link/(?P<pk>\d+)/$', LinkDetailView.as_view(), name='link_detail'),
    url(r'^link/update/(?P<pk>\d+)/$', LinkUpdateView.as_view(), name='link_update'),
    url(r'^link/delete/(?P<pk>\d+)/$', LinkDeleteView.as_view(), name='link_delete'),

    # votes
    url(r'^vote/$', VoteFormView.as_view(), name="vote"),
]

urlpatterns += [

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        base_views.root_txt_files, name='root-txt-files'),

    # Rest API
    url(r'^api/', include(router.urls)),

    # Browsable API
    url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),

    # Django Admin
    url(r'^{}/'.format(settings.DJANGO_ADMIN_URL), include(admin.site.urls)),

    # Django Registration
    url(r'^accounts/', include('registration.backends.simple.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.API_DEBUG:
    urlpatterns += [
        # Browsable API
        url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),
    ]

if settings.DEBUG:
    # Livereloading
    urlpatterns += [url(r'^devrecargar/', include('devrecargar.urls', namespace='devrecargar'))]

    urlpatterns += [
        url(r'^400/$', dj_default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', dj_default_views.permission_denied, kwargs={'exception': Exception("Permission Denied!")}),
        url(r'^404/$', dj_default_views.page_not_found, kwargs={'exception': Exception("Not Found!")}),
        url(r'^500/$', handler500),
    ]
