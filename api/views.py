from django.shortcuts import render
from .models import Movie, Rating
from .serializer import MoviSerilizer,RatingSerilizers,UserSerilizer
from rest_framework  import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerilizer
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MoviSerilizer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie=Movie.objects.get(id=pk)
            #user=User.objects.get(id=request.data['user'])
            user=request.user
            stars=request.data['stars']
           

            try:
                rating=Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars=stars
                if 'Comment' in request.data:
                    comment=request.data['Comment']
                    rating.Comment=comment
                rating.save()
                serilizers=RatingSerilizers(rating,many=False)
                response={'message':'Message Update','data':serilizers.data}
                
                
            except:
                if 'Comment' in request.data:
                    comment=request.data['Comment']
                    
                else:
                    comment=None
                
                rating=Rating.objects.create(user=user,movie=movie,stars=stars,Comment=comment)
                serilizers=RatingSerilizers(rating,many=False)
                response={'message':'Message Update','data':serilizers.data}
                
            return Response(response, status=status.HTTP_200_OK)
        else:
            response={'Stars':'You need to provide stars'}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerilizers   
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)# for authentication purpose, once authenticate token pass then only call the view class
    def update(self, request, *args,**kwargs):
        response={"message":"You can't update rating like this way"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def create(self,request, *args, **kwargs):
        response={"message":"You cant't create rating like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)