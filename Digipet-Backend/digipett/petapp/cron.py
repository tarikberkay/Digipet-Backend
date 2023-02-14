from django_cron import CronJobBase, Schedule
from django.utils import timezone
from petapp.models import PetModel,UserModel

from datetime import timedelta

class MyCronJob(CronJobBase):
   
    RUN_EVERY_MINS = 60 # every 1 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'petapp.my_cron'    # a unique code

    def do(self):
        now = timezone.now() + timedelta(hours = 3)
        q_object = PetModel.objects.all().filter(pet_active = True)
        
        for objects in q_object:
            s_time = objects.sleep_time
            f_time = objects.eating_time
            p_time = objects.pet_time
            w_time = objects.water_time


            s_diff = now-s_time
            p_diff = now - p_time
            f_diff = now - f_time
            w_diff = now- w_time

        

            if divmod(s_diff.total_seconds(),3600)[0] >=12:
                objects.sleep_level =objects.sleep_level-1.25
                if objects.sleep_level <=0:
                    objects.sleep_level = 0

            if divmod(w_diff.total_seconds(),3600)[0] >=3:
                objects.water_level =objects.water_level-3-34
                if objects.water_level <0:
                    objects.water_level = 0
                
            if divmod(f_diff.total_seconds(),3600)[0] >=4:
                objects.hunger_level =objects.hunger_level-2.25
                if objects.hunger_level <0:
                    objects.hunger_level = 0

            if divmod(p_diff.total_seconds(),3600)[0] >=4:
                objects.happiness_level =objects.happiness_level-2.25
                if objects.happiness_level <0:
                    objects.happiness_level = 0  


            h_list = [objects.sleep_level,objects.happiness_level,objects.hunger_level,objects.water_level]  
            zero_levels = 0
            full_levels = 0 

            for a in h_list:
                if a == 0:
                    zero_levels +=1
            
            
            if zero_levels>0:
                objects.hp_level = objects.hp_level - 0.5*zero_levels
                if objects.hp_level ==0:
                    objects.pet_active = False
                    objects.owner.realibility_number -=20
                    
                    
            for b in h_list:
                if b ==10:
                    full_levels+=1

            
            if full_levels ==4:
                if objects.hp_level<10:
                    objects.hp_level += 0.5*full_levels
                    if objects.hp_level>10:
                        objects.hp_level = 10
                        objects.owner.realibility_number +=10
        


            objects.save()

        
                

            


            
        return "Done!"
