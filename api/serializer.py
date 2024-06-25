from rest_framework import serializers
from .models import Movie,Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class MoviSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=('id','title','avg_ratings','no_of_ratings','description',)
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password')
        extra_kwargs={'password':{'write_only':True, 'required':True}}
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)

        return user
class RatingSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('id','movie','user','stars','Comment')
