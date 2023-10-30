from .models import User, Weight
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, WeightSerializer, LoginSerializer

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def loginUser(request, username, password):
    try:
        user = User.objects.get(username=username, password=password)
        serializer = UserSerializer(user, many=False)

        return Response(serializer.data)

    except User.DoesNotExist:
        return Response("Error logging in", status=400)


@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Error creating user", status=400)


@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(f"Updated {user.name}")
    else:
        return Response(f"Error updating {user.name}", status=400)


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response(f"Deleted user {user.name}")

# weight viewset

@api_view(['GET'])
def getWeights(request):
    weights = Weight.objects.all()
    serializer = WeightSerializer(weights, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserWeights(request, pk):
    weights = Weight.objects.filter(user=pk)
    serializer = WeightSerializer(weights, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLastUserWeight(request, pk):
    weight = Weight.objects.filter(user=pk).last()
    serializer = WeightSerializer(weight, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateWeight(request, pk):
    weight = Weight.objects.get(id=pk)
    serializer = WeightSerializer(instance=weight, data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(f"Updated {weight.weight}")
    else:
        return Response(f"Error updating {weight.weight}")

@api_view(['POST'])
def addWeight(request):
    serializer = WeightSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Error creating item")

@api_view(['DELETE'])
def deleteWeight(request, pk):
    weight = Weight.objects.get(id=pk)
    weight.delete()
    return Response(f"Deleted weight {weight.weight}")
