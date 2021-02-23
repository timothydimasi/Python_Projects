# the parent class
class Device:
    type_of_device = "Unknown"
    purpose = "Unknown"

    def info(self):
        msg = "This device is a {} used for {}.".format(self.type_of_device, self.purpose)
        return msg


# the first child class
class Cell_Phone(Device):
    type_of_device = "phone"
    manufacturer = "Apple"
    model = "10"
    purpose = "making calls"

    def info(self):
        msg = "This {} is a {} {} used for {}.".format(self.type_of_device, self.manufacturer, self.model, self.purpose)
        return msg


# the second child class
class Laptop(Device):
    type_of_device = "computer"
    purpose = "browsing the web"
    keyboard = True
    wifi = True

    def info(self):
        msg = "This is a {} used for {}.".format(self.type_of_device, self.purpose)
        return msg



cell_phone = Cell_Phone()
print(cell_phone.info())

laptop = Laptop()
print(laptop.info()) 
    



