from rest_framework import generics, mixins
from .serializers import PostSerializer, ThreadSerializer, RecursoSerializer, ArchivoSerializer,User_stats_serializer, ClubSerializer, PlantasSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Post, Thread, Recurso, Archivo, Club,Plantas
from accounts.models import UserProfile
from django.http import Http404
from rest_framework_mongoengine import viewsets
from django.http import JsonResponse

from rest_framework.permissions import AllowAny


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

class Thread_stats(APIView):

    def get(self,request):
        threads= Thread.objects.all()
        serializer = ThreadSerializer(threads,many=True)
        return Response(serializer.data)

    def post():
        pass

class ThreadAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'categoria'
    serializer_class = ThreadSerializer

    def get_queryset(self):
        cat = self.kwargs.get('categoria')
        return Thread.objects.filter(category=cat)

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ThreadRudView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.all()

class RecursoViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    serializer_class = RecursoSerializer

    def get_queryset(self):
        return Recurso.objects.all()

    def retrieve(self,request, pk=None):
        if pk.isdigit()==True:
            queryset = Recurso.objects.filter(usuario=pk)
        else:
            queryset = Recurso.objects.filter(tags__contains=pk)
        serializer = RecursoSerializer(queryset,many=True)
        return Response(serializer.data)

    def showFiles(self,request):
        result= Recurso.objects.values_list('tags')
        tags= [x.lower() for l in result for x in l]
        results=[]
        for t in set(tags):
            results.append({'tag':t,'counts':tags.count(t)})
        print(results)
        return Response(results)

    def partial_update(self, request, pk=None):
        testmodel = Recurso.objects.filter(id=pk)[0]
        serializer = RecursoSerializer(testmodel, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")

class ArchivoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = ArchivoSerializer

    def get_queryset(self):
        return Archivo.objects.all()


class User_stats(APIView):

    def get(self,request):
        user= UserProfile.objects.all()
        serializer = User_stats_serializer(user,many=True)
        return Response(serializer.data)

    def post():
        pass

class User_stats_by_id(APIView):

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(user=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = User_stats_serializer(user)
        return Response(serializer.data)


class ClubAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ClubSerializer

    def get_queryset(self):
        return Club.objects.all()

class PlantasLastAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PlantasSerializer

    def get_queryset(self):

        #list = Plantas.objects.filter(id=Plantas.objects.latest('id').id)
        list = Plantas.objects.order_by('-id')[:1]
        return list

class PlantasAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = (AllowAny,)
    lookup_field = 'pk'
    serializer_class = PlantasSerializer

    def get_queryset(self):
        return Plantas.objects.order_by('-id')
        #return Plantas.objects.order_by('-id')[:10]

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)