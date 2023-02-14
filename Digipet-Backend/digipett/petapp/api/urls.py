from django.urls import path

from .views import UserList, UserDetail,PetList, PetDetail,PetWaterAPIView,PetLoveAPIView,PetSleepAPIView, PetFoodAPIView, PetLevelDetailAPIView

urlpatterns = [
    path('user', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),

    path('user/pet', PetList.as_view()),
    path('user/pet/<int:pk>', PetDetail.as_view()),

    path('user/pet/<int:pk>/level/water/', PetWaterAPIView().as_view(), name = 'pet-water-level'),
    path('user/pet/<int:pk>/level/love/', PetLoveAPIView.as_view(), name='pet-love-level'), 
    path('user/pet/<int:pk>/level/food/',PetFoodAPIView.as_view(), name = 'pet-food-level'),
    path('user/pet/<int:pk>/level/sleep/',PetSleepAPIView.as_view(), name = 'pet-sleep-level'),

    path('user/pet/levels/<int:pk>', PetLevelDetailAPIView.as_view(), name = 'pet-levels' ),



]
