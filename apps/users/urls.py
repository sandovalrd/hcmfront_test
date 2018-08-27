from django.conf.urls import url
from .views import RegisterUsers


urlpatterns = [
	url(r'^register/$', RegisterUsers.as_view(), name='register'),
]