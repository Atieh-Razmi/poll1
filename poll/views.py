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
from django.shortcuts import get_object_or_404



class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name',]
    ordering_fields = ['total_vote',]
    permission_classes = [AllowAny,]
    filterset_fields = ['category',]


    @action(detail=True, methods=['post'])
    def vote(self,request, pk=None):
        poll = get_object_or_404(Poll, pk=pk)
        choice_id = request.data.get('choice_id')
        if not choice_id:
            return Response({"error": "You didn't select a choice."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            selected_choice = poll.choices.get(pk=choice_id)
            if Vote.objects.filter(user=request.user, choice=selected_choice).exists():
                return Response({"error": "you vote this choice before"}, status=status.HTTP_400_BAD_REQUEST)
            selected_choice.vote_count += 1
            vote = Vote.objects.create(user=request.user, choice=selected_choice)
            selected_choice.save()
            return Response({"message": "Vote recorded successfully!"})
        except Choice.DoesNotExist:
            return Response({"error": "Invalid choice selected."}, status=status.HTTP_400_BAD_REQUEST)       