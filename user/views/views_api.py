from django.core.exceptions import ValidationError
from ..models import CustomUser
from ..serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
import jwt, datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from barter.models import Wishlist

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch') # ChatGPT used for this line
class RegisterAPIView(APIView):
    permission_classes = [AllowAny] # ChatGPT also used for this line
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError('Invalid Data!')
        
        created_user = serializer.save()

        Wishlist.objects.create(
            user = created_user,
            item_list = {}
        )

        return Response({
            "message": "User registered successfully!"
        })
    
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')
        
        payload = {
            'id': user.id,
            'exp': timezone.now() + datetime.timedelta(minutes=60),
            'iat': timezone.now(),
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'Success',
            'jwt': token,
        }

        return response
    
class UserAPIView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = CustomUser.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout successfull!'
        }

        return response