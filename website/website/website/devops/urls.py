from django.conf.urls import url
from . import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.


    # The home page
    url(u'^$', views.devops_login, name='devops_login'),

    url(u'^user_check',views.user_check,name='user_check'),
    url(u'^logout',views.devops_login,name='devops_login')
]