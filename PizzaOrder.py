import csv
class PizzaOrders:
    pizza_description=""
    pizza_cost=0
    sauce_description=""
    sauce_cost=0
    name_surname=""
    tckimlikno=""
    creditcardnumber=""
    creditpass=""
    date=""
    def __init__(self):
        description=""
        cost=0
    def gotocsv(self):
        data=[self.date,self.name_surname,self.tckimlikno,self.creditcardnumber,self.creditpass,self.pizza_description+"\n"+self.sauce_description,self.pizza_cost+self.sauce_cost]
        with open("Orders.csv","a",encoding="UTF8",newline='') as f:
            writer=csv.writer(f)
            writer.writerow(data)
