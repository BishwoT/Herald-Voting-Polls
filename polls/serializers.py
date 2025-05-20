from rest_framework import serializers
from .models import Poll, Option, Vote, Favorite
from django.db.models import Count

# Option serializer with votes count
class OptionSerializer(serializers.ModelSerializer):
    votes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Option
        fields = ['id', 'option_text', 'votes_count']

# Poll serializer with nested options and vote counts
class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)  # Show username or __str__

    class Meta:
        model = Poll
        fields = ['id', 'question_text', 'created_by', 'pub_date', 'expiry_date', 'options']

# Serializer to create Poll including options and poll duration (in hours)
class PollCreateSerializer(serializers.ModelSerializer):
    options = serializers.ListField(
        child=serializers.CharField(max_length=200),
        write_only=True
    )
    duration_hours = serializers.IntegerField(write_only=True)

    class Meta:
        model = Poll
        fields = ['question_text', 'options', 'duration_hours']

    class PollCreateSerializer(serializers.ModelSerializer):
        options = serializers.ListField(
        child=serializers.CharField(max_length=200),
        write_only=True
    )
    duration_hours = serializers.IntegerField(write_only=True)

    class Meta:
        model = Poll
        fields = ['question_text', 'options', 'duration_hours']

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        duration_hours = validated_data.pop('duration_hours')
        user = self.context['request'].user

        # Remove created_by if it exists in validated_data to avoid duplication error
        validated_data.pop('created_by', None)

        from django.utils import timezone
        from datetime import timedelta

        pub_date = timezone.now()
        expiry_date = pub_date + timedelta(hours=duration_hours)

        poll = Poll.objects.create(
            created_by=user,
            pub_date=pub_date,
            expiry_date=expiry_date,
            **validated_data
        )
        for option_text in options_data:
            Option.objects.create(poll=poll, option_text=option_text)

        return poll


# Vote serializer (create only)
class VoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Vote
        fields = ['id', 'poll', 'option', 'user']

# Favorite serializer
class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    poll = PollSerializer(read_only=True)
    poll_id = serializers.PrimaryKeyRelatedField(
        queryset=Poll.objects.all(), source='poll', write_only=True
    )

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'poll', 'poll_id']
