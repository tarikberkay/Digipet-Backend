from rest_framework import serializers


from ..models import UserModel,PetModel


class PetSerializer(serializers.ModelSerializer):


    #owner = serializers.StringRelatedField() #id yerine nick geliyor

    #owner = UserModelSerializer()

    class Meta:
        model = PetModel
        fields = ['id','category','pet_name','owner','hp_level','sleep_level','sleep_time',
                  'hunger_level','eating_time','water_level','water_time','happiness_level','pet_time','story','pet_img','nickname','pet_active']

        read_only_fields  = ['sleep_level','hunger_level','water_level','happiness_level','eating_time','water_time','pet_time','sleep_time','hp_level']
    
    
    




    


 



    

class PetSleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = ['id','sleep_level','sleep_time']

    def validate_sleep_level(self, sleep):
        if sleep>10 or sleep<0:
            raise serializers.ValidationError('10>=happiness_level<=0 olabilir.')
        else:
            return sleep



class PetFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = ['id','hunger_level','eating_time']

    def validate_hunger_level(self, hunger):
        if hunger>10 or hunger<0:
            raise serializers.ValidationError('10>=happiness_level<=0 olabilir.')
        else:
            return hunger


class PetLoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetModel
        fields = ['id','happiness_level','pet_time']



    def validate_happiness_level(self, happiness):
        if happiness>10 or happiness<0:
            raise serializers.ValidationError('10>=happiness_level<=0 olabilir.')
        else:
            return happiness





class PetWaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetModel
        fields = ['id','water_level','water_time']
        
    def validate_water_level(self,water):
        if water>10 or water<0:
            raise serializers.ValidationError('10>=water_level<=0 olabilir')
        else:
            return water
    
    
    
    
class PetLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetModel
        fields = ['id','hp_level','water_level','sleep_level','hunger_level','happiness_level']
    
    
class UserModelSerializer(serializers.ModelSerializer):

    MY_PETS = PetSerializer(read_only = True, many = True )
    class Meta:
        model = UserModel
        fields = ['id','username','password','email','realibility_number','is_active','first_name','last_name','MY_PETS']



        


