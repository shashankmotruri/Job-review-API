
from rest_framework import filters
from rest_framework import status
from rest_framework import generics,status,views

from rest_framework.response import Response
from .serializers import CandidateSerializer
from .models import Candidate

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.decorators import api_view

class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','age']

class CandidateUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


