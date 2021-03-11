# example of a class that utilizes both private and protected attributes or functions
# this example class will be 'Car' and it will have two attributes: motor and doors
class Car:
    def __init__(self, motor, doors):
        self._motor = motor
        self.__doors = doors

    def carInfo(self):
        print(self._motor)
        print(self.__doors)

# now, I create an actual instance of 'Car' in the form of 'audi1' and
# call on the class function 'carInfo()' to show that both statements
# should print because we are operating from within the class and not outside of it
audi1 = Car('V8',4)
audi1.carInfo()

# if this code works, the first statement should print and the second should produce an error
# this is because the double underscore actually blocks it from being used outside the class
# while the single underscore is more of a convention 
print('Below, we will try accessing from outside of the class.')
print(audi1._motor)
print(audi1.__doors)