from django.urls import path
 
from .views import IndexView, SupportView, ContactView
 
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('support/', SupportView.as_view(), name="support"),
    path('support/contact/', ContactView.as_view(), name="contact"),
]