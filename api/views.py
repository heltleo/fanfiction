import json
from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions, views, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework.throttling import ScopedRateThrottle
from api.models import Fanfic
from api.models import Comment
from api.models import Chapter
from api.models import Category
from api.models import SubCategory
from api.models import FlatPages
from api.models import FoireAuxQuestions
from api.serializers import ChapterSerializer
from api.serializers import CommentSerializer
from api.serializers import CommentCreateSerializer
from api.serializers import CategorySerializer
from api.serializers import SubCategorySerializer
from api.serializers import GenresSerializer
from api.serializers import ClassementSerializer
from api.serializers import StatusSerializer
from api.serializers import FlatPagesSerializer
from api.serializers import FoireAuxQuestionsSerializer
from api import custompermission

"""
Liste des genres
"""

class GenresList(generics.ListAPIView):
    queryset = Fanfic.objects.all()[:1]
    serializer_class = GenresSerializer
    pagination_class = None
    permission_classes = (
        permissions.AllowAny,
    )
    name='genre-list'


"""
Liste de classement
"""

class ClassementList(generics.ListAPIView):
    queryset = Fanfic.objects.all()[:1]
    serializer_class = ClassementSerializer
    pagination_class = None
    permission_classes = (
        permissions.AllowAny,
    )
    name='classement-list'


"""
Liste des status
"""

class StatusList(generics.ListAPIView):
    queryset = Fanfic.objects.all()[:1]
    serializer_class = StatusSerializer
    pagination_class = None
    permission_classes = (
        permissions.AllowAny,
    )
    name='status-list'


"""
FlatPages
"""

class FlatPagesView(generics.ListAPIView):
    """docstring for FlatPagesView."""
    queryset = FlatPages.objects.all()
    serializer_class = FlatPagesSerializer
    pagination_class = None
    permission_classes = (
        permissions.AllowAny,
    )
    name = 'all-pages'


class FlatPagesByTypeView(generics.RetrieveAPIView):
    """docstring for FlatPagesByTypeView."""
    queryset = FlatPages.objects.all()
    serializer_class = FlatPagesSerializer
    pagination_class = None
    permission_classes = (
        permissions.AllowAny,
    )
    lookup_field = 'type'
    name = 'pages'



"""
Liste des chapitres
"""

class ChapterListView(generics.ListAPIView):
    serializer_class = ChapterSerializer
    name='chapter-list'
    permission_classes = (
        permissions.AllowAny,
    )
    pagination_class = None

    def get_queryset(self):
        fanfic = self.kwargs['fanfic']
        return Chapter.objects.filter(fanfic=fanfic)



class ChapterCreateView(generics.CreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    name='chapter-create'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = None



class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    name='chapter-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

"""
Liste des catégories
"""

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    name='category-list'
    filter_fields = (
        'name',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )
    pagination_class = None


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    name='category-detail'


"""
Liste des sous-catégories
"""

class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    name='subcategory-list'
    pagination_class = None


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    name='subcategory-detail'


"""
Liste des questions/réponses pour la FAQ
"""

class FoireAuxQuestionsList(generics.ListAPIView):
    queryset = FoireAuxQuestions.objects.all()
    serializer_class = FoireAuxQuestionsSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    name = 'faq-list'
    pagination_class = None


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'fanfics-list-remastered': reverse('fanfic-list-remastered', request=request),
            'chapters': reverse('chapter-create', request=request),
            'comments': reverse('comment-list', request=request),
            'category': reverse('category-list', request=request),
            'sub-category': reverse('subcategory-list', request=request),
            'users': reverse('user-list', request=request),
            'posts' : reverse('post-list', request=request),
            'genres': reverse('genre-list', request=request),
            'status': reverse('status-list', request=request),
            'classements': reverse('classement-list', request=request),
            'faq': reverse('faq-list', request=request),

        })
