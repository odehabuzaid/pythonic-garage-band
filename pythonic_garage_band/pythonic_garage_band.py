



from abc import abstractclassmethod


class Musician:
    def __init__(self, name):
        self.name = name
    def __repr__(self): 
        return "| %s |" % self.name    
    def __str__(self):
        return "| %s |" % self.name


class Band(Musician):
    instances = []
    
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)
    def play_solos(self):
        solos = [i.play_solo() for i in self.members]
        return solos

    def __str__(self):
        return '%s' % self.name
    def __repr__(self):
        return '%s' % self.name

    @classmethod
    def to_list(cls):
        bands = [i[0].name for i in cls.instances]
        return bands
    
@abstractclassmethod
class Keyboardist(super):
    def __init__(self,keyboardist) :
        self.keyboardist = keyboardist
        
    @abstractclassmethod
    def some_methid(self):
        return '%s' % self.keyboardist
    

    
    
    
    @classmethod
    def to_list(cls):
        return cls.instances
    def __repr__(self):
        return "| %s |" % self.name
    def __str__(self):
        return "| %s |" % self.name               


class Guitarist(Musician):
    def __str__(self):
        return "My name is %s and I play guitar" % self.name
    def __repr__(self):
        return "Guitarist instance. Name = %s" % self.name
     
    def get_instrument(self):
        return "guitar"
    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician):
    def __str__(self):
        return "My name is %s and I play drums" % self.name
    
    def __repr__(self):
        return  "Drummer instance. Name = %s"% self.name
   
    def get_instrument(self):
        return "drums"
    def play_solo(self):
        return "rattle boom crash"

class Bassist(Musician):
    def __str__(self):
        return "My name is %s and I play bass" % self.name
    def __repr__(self):
        return "Bassist instance. Name = %s"% self.name
    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"
