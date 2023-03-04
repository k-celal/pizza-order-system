class Pizza:
    name=""
    cost=0
    size=""
    def __init__(self,pizzaCode,boyut):
        self.size = boyut
        if ClassicPizza.code==pizzaCode:
            self.name=ClassicPizza.name
            self.cost=ClassicPizza.cost
        elif MargaritaPizza.code==pizzaCode:
            self.name = MargaritaPizza.name
            self.cost = MargaritaPizza.cost
        elif TurkPizza.code==pizzaCode:
            self.name = TurkPizza.name
            self.cost = TurkPizza.cost
        elif PlainPizza.code==pizzaCode:
            self.name = PlainPizza.name
            self.cost = PlainPizza.cost
        else:
            self.cost=0
    def get_description(self):
        return self.size+" "+self.name
    def get_cost(self):
        if self.size=="Small":
            return self.cost+25
        elif self.size=="Medium":
            return self.cost+50
        else:
            return self.cost+75
class ClassicPizza(Pizza):
    code="01"
    name="Classic Pizza"
    cost=100
class MargaritaPizza(Pizza):
    code="02"
    name="Margarita"
    cost=200
class TurkPizza(Pizza):
    code="03"
    name="Turk Pizza"
    cost=100
class PlainPizza(Pizza):
    code="04"
    name="Plain Pizza"
    cost=125