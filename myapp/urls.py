
from django.urls import path
from .import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('home/',views.home_page,name='home'),
    path('logout/',views.logout_view,name='logout')

]
