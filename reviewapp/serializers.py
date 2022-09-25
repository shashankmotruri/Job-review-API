from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ("name","age","resume","gender","status")
        extra_kwargs = {'created_by': {'read_only':True}}
