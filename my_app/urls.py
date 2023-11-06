from django.urls import path
from my_app.views import login_view, logout_view, index_view, contact_view, about_view, portfolio_view, service_view

urlpatterns = [

    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('service/', service_view, name='service'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
