from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, FreelanceSignupView, ClientSignupView

class FreelanceSignupView(generics.GenericAPIView):
    serializer_class=FreelanceSignupView
    def post(self, request, *args, **kwargs):
             serializer=self.get_serializer(data=request.data)
             serializer.is_valid(raise_exception=True)
             user=serializer.save()
             return Response({
                 "user":UserSerializer(user, context=self.get_serializer_context()).data,
                 "token":Token.objects.get(user=user).key,
                 "message":"Account created successfully"
                  
             })
             
    
             
class ClientSignupView(generics.GenericAPIView):
    serializer_class=ClientSignupView
    def post(self, request, *args, **kwargs):
             serializer=self.get_serializer(data=request.data)
             serializer.is_valid(raise_exception=True)
             user=serializer.save()
             return Response({
                 "user":UserSerializer(user, context=self.get_serializer_context()).data,
                 "token":Token.objects.get(user=user).key,
                 "message":"Account created successfully"
                  
             })
             
             