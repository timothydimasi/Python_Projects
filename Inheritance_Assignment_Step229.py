# Parent class definition
class Homes:
    bedrooms = 0
    bathrooms = 0
    square_footage = 0
    # is this how you create an empty boolean variable within a class definition?
    covered_parking = ' '
    heat_source = ' '

# child class definitions
class House(Homes):
    garage = ' '
    pool = ' '

class Apartment(Homes):
    mail_on_site = ' '
    type_of_key = ' ' 
