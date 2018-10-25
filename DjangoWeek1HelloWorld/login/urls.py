from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include, url

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^login/$',login),
#     url(r'^logout/$',logout),
#     url(r'^welcome/$',welcome),
#     path('', views.login,name='login'),
# 	path('welcome/', views.welcome,name='welcome'),
# 	path('logout/', views.logout,name='logout'),
# ]