from rest_framework.serializers import HyperlinkedModelSerializer
from article.models import Article
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from Authorization.models import User

class ArticleSerializer(HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Article
        fields = ('id','user', 'article_name','category','description')
        
    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user',instance.user)
        instance.article_name = validated_data.get('article_name',instance.article_name)
        instance.description = validated_data.get('description',instance.description)
        instance.category = validated_data.get('category',instance.category)
        return instance
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'bio', 'email')
    
