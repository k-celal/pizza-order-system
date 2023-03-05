class Sos:
    Sauce=[]
    cost=0
    def __init__(self,args):
        self.Sauce=[]
        for i in args:
            if Olive.name==i:
                self.Sauce.append(i)
                self.cost+=Olive.cost
            elif MushRoom.name==i:
                self.Sauce.append(i)
                self.cost += MushRoom.cost
            elif GoatCheese.name==i:
                self.Sauce.append(i)
                self.cost += GoatCheese.cost
            elif Meat.name==i:
                self.Sauce.append(i)
                self.cost += Meat.cost
            elif Onion.name==i:
                self.Sauce.append(i)
                self.cost += Onion.cost
            elif Corn.name==i:
                self.Sauce.append(i)
                self.cost+=Corn.cost
            else:
                self.cost+=0
    def get_description(self):
        describtion=""
        for i in self.Sauce:
            describtion+=i+"\n"
        return describtion
    def get_cost(self):
        return self.cost
class Olive(Sos):
    name="Olive"
    cost=15
class MushRoom(Sos):
    name="MushRoom"
    cost=20
class GoatCheese(Sos):
    name="GoatCheese"
    cost=45
class Meat(Sos):
    name="Meat"
    cost=35
class Onion(Sos):
    name = "Onion"
    cost = 15
class Corn(Sos):
    name = "Corn"
    cost = 10
