
from questions.models import Question
from .serializers import QuestionSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
   # permission_classes = (IsAuthenticated,)




    #  authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    




# from rest_framework.generics import (
#      ListAPIView,
#      RetrieveAPIView,
#      CreateAPIView,
#      DestroyAPIView,
#      UpdateAPIView
#      )

# class QuestionListView(ListAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class QuestionDetailView(RetrieveAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class QuestionCreateView(CreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class QuestionUpdateView(UpdateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class QuestionDeleteView(DestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
