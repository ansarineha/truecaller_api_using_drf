from django.urls import path
from .views import ContactList,Register,Login,MarkSpam,SearchName,SearchPhoneNumber


urlpatterns=[
	path('register/',Register.as_view(),name='register'),
	path('login/',Login.as_view(),name='login'),
	path('contacts/',ContactList.as_view(),name='contacts'),
	path('spams/',MarkSpam.as_view(),name='spams'),
	path('search_by_name/',SearchName.as_view(),name='search_name'),
	path('search_by_phone_number/',SearchPhoneNumber.as_view(),name='search_phone_number')
]
