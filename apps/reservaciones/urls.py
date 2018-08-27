from django.conf.urls import url
from .views import ReservarList, ReservarDetail, ReservarDelete, ReservarUpdate, ReservarCreate, EstatusReserva, CambiarEstatusReserva, ReservarEstatusDetail


urlpatterns = [
	url(r'^list/$', ReservarList.as_view(), name='reservar-list'),
	url(r'^detail/(?P<pk>[0-9]+)/$', ReservarDetail.as_view(), name='reservar-detail'),
	url(r'^delete/(?P<pk>[0-9]+)/$', ReservarDelete.as_view(), name='reservar-delete'),
	url(r'^update/(?P<pk>[0-9]+)/$', ReservarUpdate.as_view(), name='reservar-update'),
	url(r'^create/$', ReservarCreate.as_view(), name='reservar-create'),
	url(r'^status/list$', EstatusReserva.as_view(), name='reservar-estatus-list'),
	url(r'^status/update/(?P<pk>[0-9]+)/$', CambiarEstatusReserva.as_view(), name='reserva-estatus-update'),
	url(r'^status/detail/(?P<pk>[0-9]+)/$', ReservarEstatusDetail.as_view(), name='reservar-estatus-detail'),
]