from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Prefetch
from .models import Poll, Option, Vote, Favorite
from .serializers import PollSerializer, PollCreateSerializer, VoteSerializer, FavoriteSerializer
from rest_framework.decorators import api_view, permission_classes


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Base queryset with options annotated with votes count
        base_qs = Poll.objects.all().prefetch_related(
            Prefetch('options', queryset=Option.objects.annotate(votes_count=Count('vote')))
        )

        # Customize queryset based on action
        if self.action == 'browse':
            # For browse page, return all polls or filter for recommended, popular, recent
            return base_qs

        elif self.action == 'mypolls':
            # Polls created by current user
            return base_qs.filter(created_by=user)

        elif self.action == 'results':
            # Polls the user voted on
            voted_polls_ids = Vote.objects.filter(user=user).values_list('poll_id', flat=True)
            return base_qs.filter(id__in=voted_polls_ids)

        return base_qs

    def get_serializer_class(self):
        if self.action == 'create':
            return PollCreateSerializer
        return PollSerializer

    @action(detail=False, methods=['get'])
    def browse(self, request):
        # You can add logic here for recommended, popular, recent
        polls = self.get_queryset()
        # Example: separate categories (simplified)
        recommended = polls.order_by('-pub_date')[:5]
        popular = polls.annotate(num_votes=Count('vote')).order_by('-num_votes')[:5]
        recent = polls.order_by('-pub_date')[:5]

        # Serialize separately
        recommended_ser = PollSerializer(recommended, many=True)
        popular_ser = PollSerializer(popular, many=True)
        recent_ser = PollSerializer(recent, many=True)

        return Response({
            'recommended': recommended_ser.data,
            'popular': popular_ser.data,
            'recent': recent_ser.data
        })

    @action(detail=False, methods=['get'])
    def mypolls(self, request):
        user = request.user
        polls = self.get_queryset().filter(created_by=user)
        serializer = self.get_serializer(polls, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def results(self, request):
        polls = self.get_queryset()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        poll = self.get_object()
        user = request.user
        option_id = request.data.get('option_id')

        # Check if already voted
        if Vote.objects.filter(poll=poll, user=user).exists():
            return Response({'detail': 'You have already voted on this poll.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate option
        try:
            option = poll.options.get(pk=option_id)
        except Option.DoesNotExist:
            return Response({'detail': 'Invalid option.'}, status=status.HTTP_400_BAD_REQUEST)

        # Save vote
        Vote.objects.create(poll=poll, option=option, user=user)
        return Response({'detail': 'Vote recorded successfully.'})

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        poll = self.get_object()
        if poll.created_by != request.user:
            return Response({'detail': 'You can only delete your own polls.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class FavoriteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
