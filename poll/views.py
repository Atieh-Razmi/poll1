from django.shortcuts import render
from rest_framework.response import Response
from .models import Poll, Choice, Vote
from .serializers import PollSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ['category__name',]
    permission_classes = [AllowAny,]


    @action(detail=True, methods=['post'])
    def vote(self,request, pk):
        poll = self.get_object()
        choice_id = request.data.get('choice_id')
        try:
            choice = poll.choices.get(id=choice_id)
        except Choice.DoesNotExist:
            return Response({'error':'not exist'})

        vote = Vote.objects.create(user=request.user, choice=choice)
        return Response({'message':'create'})       