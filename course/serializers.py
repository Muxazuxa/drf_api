from rest_framework import serializers
from course.models import Course, Contacts, Branches

class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = ('id', 'type', 'value')


class BranchesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = ('id', 'address', 'latitude', 'longitude')


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True)
    branches = BranchesSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')

    def create(self, validated_data):
        return Course.objects.create(**validated_data)