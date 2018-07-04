
from rest_framework import generics
from course.models import Course
from course.serializers import CourseSerializer


class course_list(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class course_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer