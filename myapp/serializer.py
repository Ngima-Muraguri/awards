from rest_framework import serializers
from .models import Projects, Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'title', 'image', 'description', 'live_link', 'posted_by', 'date_posted')


        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'profile_pic', 'bio', 'contact' )