from .models import Poll, Vote, Choice
from rest_framework import serializers


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__' 


class ChoiceSerializer(serializers.ModelSerializer):
    vote = VoteSerializer(many=True)
    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many = True)
    
    #total_vote = serializers.readonlyfield()
    total_vote = serializers.SerializerMethodField()
    class Meta:
        model = Poll
        fields = '__all__'

    def get_total_vote(self, obj):
        return obj.total_vote    


 

       
