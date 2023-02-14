from ..models import UserModel, PetModel
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView, ListAPIView, RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserModelSerializer, PetSerializer,PetLoveSerializer, PetWaterSerializer, PetSleepSerializer, PetFoodSerializer,PetLevelSerializer




class UserList(ListCreateAPIView):
   
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]

class UserDetail(RetrieveUpdateDestroyAPIView):
    
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]


class PetList(ListCreateAPIView):
   
    queryset =PetModel.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]



class PetDetail(RetrieveUpdateDestroyAPIView):
    
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer
    permission_classes = [AllowAny]

    
     #hayvan yaşıyor mu?
    def hayvan_kontrol(self,object):
        if object.hp_level_conf == 0:
            pet_active = False
            # return 'Hayvan died'
        else:
            pet_active = True




class PetWaterAPIView(RetrieveUpdateAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetWaterSerializer
    permission_classes = [AllowAny]

    
    

class PetLoveAPIView(RetrieveUpdateAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetLoveSerializer
    permission_classes = [AllowAny]


class PetSleepAPIView(RetrieveUpdateAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetSleepSerializer
    permission_classes = [AllowAny]


class PetFoodAPIView(RetrieveUpdateAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetFoodSerializer
    permission_classes = [AllowAny]

class PetLevelDetailAPIView(RetrieveAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetLevelSerializer
    permission_classes = [AllowAny]

