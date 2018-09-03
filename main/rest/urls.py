from django.conf.urls import url, include

from main.rest.views import EndpointView

urlpatterns = [
    url(r'^endpoint/$', EndpointView.as_view(), name='endpoint'),
]

