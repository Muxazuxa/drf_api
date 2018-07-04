from django.conf.urls import url
from course import views

urlpatterns = [
    url(r'^course/$', views.course_list.as_view()),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_detail.as_view()),
]