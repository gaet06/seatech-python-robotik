import time

class Robot():

    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __states = ['shutdown', 'running']
    __charge_level = 0
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """
    #__slots__ = ('name','power','current_speed', 'battery_level', 'states')
    
    def __init__(self, name=None):
	
      if name:
	
        self.__name = name
	
      self.__current_state = self.__states[0]
      self.__power = False
      
    def allumer(self) :

       if(self.__power==False):

        self.__current_state = self.__states[1] 
        self.__power = True
        print("demarrage")
      
    def eteindre (self):

      if(self.__power==True):

       self.__current_state = self.__states[0] 
       self.__power = False
       print("extinction\n")

    def charge(self):
      print("le robot est en charge")
      while self.__charge_level<100:
        self.__charge_level = self.__charge_level + 10
        print(self.__charge_level)
        if(self.__charge_level > 100):
            self.__charge_level = 100
        time.sleep(1)

    def speed(self,vit):
      self.__current_speed = vit
      print("ma vitesse est de", self.__current_speed,"m/s")

    def stop(self):
      self.__current_speed = 0
      print("le robot est a l'arret",self.__current_speed,"m/s")
    
    def status(self):
      print("mon robot s'appelle",self.__name)
      print("le robot est en",self.__current_state)
      print("la batterie est de",self.__charge_level,"%")
      print("la vitesse est de",self.__current_speed,"m/s")


r = Robot('dudule')
r.charge()
r.allumer()
r.speed(100)
r.stop()
r.eteindre()
r.status()


