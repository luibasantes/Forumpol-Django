from rest_framework import generics, mixins
from .serializers import PostSerializer, ThreadSerializer, RecursoSerializer, ArchivoSerializer
from ..models import Post, Thread, Recurso, Archivo
from rest_framework_mongoengine import viewsets

class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class= PostSerializer

    def get_queryset(self):
        uid = self.kwargs.get("pk")
        return Post.objects.filter(owner_id=uid)


class PostRudView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()



class ThreadAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'categoria'
    serializer_class = ThreadSerializer

    def get_queryset(self):
        cat = self.kwargs.get('categoria')
        return Thread.objects.filter(category=cat)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ThreadRudView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.all()

class RecursoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = RecursoSerializer

    def get_queryset(self):
        return Recurso.objects.all()

class ArchivoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = ArchivoSerializer

    def get_queryset(self):
        return Archivo.objects.all()