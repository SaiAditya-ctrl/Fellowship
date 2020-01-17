try:
    from __future__ import generators
    import random
    rom enum import Enum, auto
except:
  print("An exception occurred")

class InventoryType(Enum):
    RICE  = auto() 
    PULSES  = auto() 


class Inventory(object):
    pass

class Rice(Inventory):
    def name(self): 
        print("Brown Rice")
        print("Rajbhoga")
        print("Kidney Beans")
    def price(self): 
        total_rice_price=0
        price=2000
        print("Brown Rice price",price)
        price1=3000
        print("Rajbhoga price",price)
        price2=4000
        print("Kidney Beans price",price)
        total_rice_price=0
        total_rice_price=price+price2+price2
        print(total_rice_price)
  

class Pulses(Inventory):
    def name(self): 
        print("Green Gram")
        print("Black lentils")
        print("Kidney Beans")
    
    def price(self): 
        price=250
        print("Brown Rice price",price)
        price1=350
        print("Black lentils price",price1)
        price2=450
        print("Green Gram",price2)
        total_pulses_price=0
        total_pulses_price=price+price2+price2
        print(total_pulses_price)
                

class InventoryFactory(object):

    @staticmethod
    def create(type):
        
        if type in InventoryFactory.choice:
            return InventoryFactory.choice[type]()

        assert 0, "No data Found: " + type    

    choice = { InventoryType.RICE:  Rice,
               InventoryType.PULSES:  Pulses                
             }


def datasNameGen(n):

    types = list(InventoryType)

    for i in range(n):
        yield random.choice(types)


data = [ InventoryFactory.create(i) for i in datasNameGen(5)]

for datas in data:
    datas.name()
    datas.price()
