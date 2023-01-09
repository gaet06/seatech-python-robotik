from exo1_starter_template import Robot

class Human():   
    # Human class content here
    __sexe = {'homme','femme','autre'}
    __aliments = []

    def __init__(self, sexe):

        self.__sexe = sexe
        
    

    def eat(self, aliment):

        if type(aliment)==str :
            self.__aliments.append(aliment)
        elif type(aliment)==list:
            self.__aliments += aliment
        else:
            print("j'ai pas graille frère ")


    def digest(self):

        if self.__aliments == []:
            print('lache un croc avant de demander ça!') 
            
        else :
            self.__aliments.clear() 

        

    @property 
    def show_aliment(self):
        print("j'ai mangé", self.__aliments)
        
    @property
    def show_sexe(self):
        print("je suis un(e)",self.__sexe)
    

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

        


cyborg = Cyborg('dagobert', 'Femme')
cyborg.show_sexe
midi=['pomme d eau fine','male tes aires']
cyborg.eat(midi)
cyborg.show_aliment
cyborg.show_name
cyborg.digest()
cyborg.allumer()


# print(cyborg.name, 'sexe', cyborg.sexe)
# print('Charging battery...')
# cyborg.charge()
# cyborg.status()
# cyborg.eat('banana')
# cyborg.eat(['coca', 'chips'])
# cyborg.digest()