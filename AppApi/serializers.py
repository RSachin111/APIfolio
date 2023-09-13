from rest_framework import serializers
from .models import WorkExperience

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'  #for all the fields 
        
        # fields= ('title','start_date','end_date') #for specific fields 