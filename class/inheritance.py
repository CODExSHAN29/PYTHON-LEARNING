class Basechai:
    def __init__(self,type_):
        self.type =type_

    def prepare(self):
        print("preparing {self.type}chai")



class masalachai(Basechai):
    def add_spices(self): 
        print("adding cardamom to{self.type}")