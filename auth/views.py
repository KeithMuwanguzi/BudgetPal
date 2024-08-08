from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from users.models import User
from . serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, email = request.data['email'])
    if user.check_password(request.data['password']):
        token, created = Token.objects.get_or_create(user = user)
        ser = UserSerializer(instance = user)
        return Response({
            'message':'Logged in successfully',
            'status':'success',
            'data':{
                'token':token.key,
                'data':ser.data
            }
        })


@api_view(['POST'])
def register(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        user = User.objects.get(name = request.data['name'])
        user.set_password(request.data['password'])
        user.save()
        token, created = Token.objects.get_or_create(user = user)
        return Response({
            'message':'New user created successfully',
            'status':'success',
            'data':{
                'token':token.key,
                'data':ser.data
            }
        })
    else:
        return Response({
            'status':'error',
            'data':ser.errors
        })

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    ser = UserSerializer(users, many=True)
    return Response({
            'status':'success',
            'data':ser.data
        })

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def testToken(request):
    return Response({
        'message':f'Test passed for {request.user.name}'
    })