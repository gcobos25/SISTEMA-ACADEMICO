from django.urls import path
from AcademicoKairos import views

urlpatterns = [
	path(
		route='',
		view=views.LoginInit.as_view(),
		name='login'
	),
]