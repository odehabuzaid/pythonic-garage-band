
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
        self.instances.append({'name': self.name, 'members': self.members})
    def play_solo(self):
        for member in self.members:
            member.play_solo()
    


    @classmethod
    def to_list(cls):
        return cls.instances
    def __repr__(self):
        return "| %s |" % self.name
    def __str__(self):
        return "| %s |" % self.name               


class Guitarist(Musician):
    def __str__(self):
        return "Guitarist %s" % self.name
    def __repr__(self):
        return "Guitarist %s " % self.name
    def get_instrument(self):
        return "Guitar"
    def play_solo(self):
        return 'Some solo is playing now %s' % self.name

class Drummer(Musician):
    def __str__(self):
        return "Drummer = %s" % self.name
    def __repr__(self):
        return "Drummer = %s" % self.name
    def get_instrument(self):
        return 'Drums'
    def play_solo(self):
        return 'Some solo is playing now %s' % self.name

class Bassist(Musician):
    def __str__(self):
        return f"Bassist = %s" % self.name
    def __repr__(self):
        return f"Bassist = %s" % self.name
    def get_instrument(self):
        return 'Bass'
    def play_solo(self):
        return 'Some solo is playing now %s' % self.name



