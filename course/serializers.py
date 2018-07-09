from rest_framework import serializers
from course.models import Course, Contact, Branch


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('type', 'value')


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('address', 'latitude', 'longitude')


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ('name', 'logo', 'description', 'category', 'contacts', 'branches')

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')

        course = Course.objects.create(**validated_data)

        for contact in contacts:
            Contact.objects.create(course=course, **contact)
        for branch in branches:
            Branch.objects.create(course=course, **branch)

        return course
