from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(["POST"])
def register_view(request):
    if request.method == "POST":
        serializer =  RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            token, _ = Token.objects.get_or_create(user=account)
            data = serializer.data
            data["token"] = token.key
        else:
            data = serializer.errors
        return Response(data)
