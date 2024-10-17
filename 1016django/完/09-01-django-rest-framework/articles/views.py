from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET' , 'POST']) # 필수
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()  # 쿼리셋형태
        serializer = ArticleListSerializer(articles , many=True) # serial형태로 변환
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        print('get success')
        serializer = ArticleSerializer(article) # serial형태로 변환
        return Response(serializer.data)
    elif request.method == 'DELETE':
        print('deleted success')
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        print('putted')
        serializer = ArticleSerializer(article, data=request.data , partial=True) # serial형태로 변환
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)