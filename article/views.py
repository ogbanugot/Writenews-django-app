from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import render, redirect
from article.serializers import UserSerializer
from article.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser
from django.contrib.auth import get_user_model
from guardian.utils import get_anonymous_user


#api for listing all articles
class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)#permission for authenticated users and owner of article

    def get_queryset(self):
        queryset = Article.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user() #handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

#api for a particular article provides PUT,PATCH and DELETE HTTP methods
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)               

#api for listing all writers
class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

#api for a particular writers 
class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
