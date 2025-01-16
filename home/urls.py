from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contact_us/', views.ContactUs.as_view(), name='contact_us'),
    path('subscribe/', views.NewsLetter.as_view(), name='subscribe'),
    path('shipping/', views.ShippingView.as_view(), name='shipping'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('policies/', views.PolicyView.as_view(), name='policies'),
]
