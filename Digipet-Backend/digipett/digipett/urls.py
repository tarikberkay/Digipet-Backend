
from django.contrib import admin
from django.urls import path,include
from dj_rest_auth.registration.views import VerifyEmailView,ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('petapp.api.urls')),

    path('auth/', include('dj_rest_auth.urls')),

   
        
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

   


   




    
]
