
        

class Musician:

    def __init__(self,name) -> None:
        self.name=name 


class Band():       #(Musician):
    
    instances=[]
    def __init__(self,name,members):
        self.name=name 
        self.members=members
        self.instances.append(self)

    def __str__(self) -> str:
        return str(self.name)

    
    def __repr__(self) :
        return str(self.name)


    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
        
        
    

    @classmethod
    def to_list(cls):
        #  returns a list of previously created Band instances
        return cls.instances

# ###################################################################################
class Guitarist(Musician):
    
    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    
    def __repr__(self) -> str:
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"
    
# ##############################################################################  
class Bassist(Musician):

    def __str__(self) -> str:
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self) -> str:
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"
    
# ###############################################################################3
class Drummer(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self) -> str:
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"




# create some musicians -------------------------------------------------------------------
# jimi = Guitarist("Jimi Hendrix")
# john = Bassist("John Paul Jones")
# neil = Drummer("Neil Peart")

# create a band and add the musicians
# band = Band("The Band",[])
# band.members.append(jimi)
# band.members.append(john)
# band.members.append(neil)
#  [jimi,john,neil]
# ask the band to play solos
# solos = band.play_solos()
# print(solos)  # should print ["guitar solo", "bass solo", "drum solo"]

# check the list of instances
# instances = Band.to_list()
# print(instances)  # should print [Band("The Band")]
# the_nobodies = Band("The Nobodies", [])
# print(the_nobodies)
# # Band.instances = []