from rest_framework import serializers
from .models import Student

class StudentSerializerRep(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'fname', 'lname', 'roll_no', 'standard', 'section']

class StudentSerializerInp(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
