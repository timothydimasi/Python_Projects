from abc import ABC, abstractmethod

# here, I am creating a class 'appliance' that inherits from the abstract base class
# the 'cost' method simply prints out the cost of an appliance once called upon and passed an argument
class appliance(ABC):
    def cost(self,amount):
        print("This appliance costs: {}".format(amount))

    # this is a bit of new syntax that I am still trying to wrap my head around
    # the abstract method 'inventory' is not actually being defined or implemented yet
    @abstractmethod
    def inventory(self, quantity):
        pass

# in this child class of 'appliance' we are now defining the abstract method for use in this subclass
class refrigerator(appliance):
    def inventory(self, quantity):
        print("There are {} refrigerators in stock.".format(quantity))


# here we create an instance of refrigerator and call upon the 'cost' and 'inventory' methods
obj = refrigerator()
obj.cost(1500)
obj.inventory(7)