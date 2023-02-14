from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import UserModel, PetModel

from requests import request

admin.site.site_title = 'DigiPet'

admin.site.site_header = 'Digipet-Administration'
admin.site.index_title = 'Welcome to Digipet-Administration'



# bir buton oluşturmuş olduk.. Adresi tam gir 
def  click_me(self):
    return format_html(f'<a href ="http://127.0.0.1:8000/admin/petapp/usermodel/{self.id}/change/">View</a>') 

#def asset_view(self):
#     return format_html(f'<img src ="http://127.0.0.1:8000/media/media/{self.asset}" style = "height:50px;width:50px>')




class CustomUserAdmin(UserAdmin):
    
    def publish(self,request,queryset): #fonksiyon ! halledildi. GO'ya bas.
        
       count = queryset.update(is_active = True)
       self.message_user(request,f"{count} adet kullanici aktif edildi!")
    
    def publish_no(self,request,queryset):

        count = queryset.update(is_active = False)
        self.message_user(request, f"{count} adet kullanici devre disi birakildi! ")

    publish.short_description = 'İşaretlenen Kullanicilar Aktif Et'
    publish_no.short_description = 'İşaretlenen Kullanicilari Devre Disi Et'
    
    actions= ['publish','publish_no']
    

    date_hierarchy = 'date_joined' #tarih sıralaması eklendi.
    


    

    list_filter = ['date_joined','is_active']
    list_display = ('username','email','date_joined','id','is_active',click_me,) #değişkenleri listeledik
    list_display_links = [click_me] #değişkenlere tıklandı mı yönlendirme işlemi
    list_editable= ['is_active']
    list_per_page = 50
    search_fields = ['username']


    # fieldsts hakkında bazı ayarlamalar
    
    fieldsets = (
        ('Personal info', {"fields": ("username", "password",'email')}),

        
        
        
        ("Account Info",
            {
                "fields": (
                    "is_active","realibility_number",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            'Additional Info',
            {
                'fields':(
                    'first_name',
                    'last_name',

                ),
                'description' : 'User için genel ayarlar'
            
            }
        )
    )

    


admin.site.register(UserModel, CustomUserAdmin)


class CustomPetModel(admin.ModelAdmin):


    # fieldsets = (
    #      ('Change My Pet', {
    #          "fields": (
    #               'pet_name',
    #               'nickname',
    #              'category',
    #               'story',
    #               'pet_img',

    #         ),
    #        'description':'Pet değiştirme ekranı'
    #      }),  )


    list_display = ['pet_name']


    



admin.site.register(PetModel,CustomPetModel)





