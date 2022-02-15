from django.core.mail import send_mail
from main.settings import FROM_EMAIL
from rest_framework import status
from rest_framework.response import Response
from tokenize import TokenError
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['email'] = self.user.email
        return data


class SendEmailWithToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        try:
            email = serializer.validated_data.get('email')
            access_token = serializer.validated_data.get('access')
            send_mail(
                'Your access token',
                access_token,
                FROM_EMAIL,
                [email],
                fail_silently=False,
            )
        except:
            'Send e-mail error'
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
