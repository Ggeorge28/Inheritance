class Customer:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone



class Car(Customer):

    def __init__(self,name,address,phone,make,model,year):

        Customer.__init__(self,name,address,phone)

        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    

    def print_person(self):
        print(f" Name:", Customer.get_name(self), " Address:", Customer.get_address(self), " Phone:", Customer.get_phone_number(self))
        #print(" Address:", Customer.get_address(self))
        #print(" Phone:", Customer.get_phone_number(self))
        print(f" Car Make: {self.__make}", " Car Model:", Car.get_model(self), " Car Year:", Car.get_year(self))
        #print(f" Car Year:", Car.get_year(self))

class Service:
    def __init__(self, pcharge, lcharge, tcharge):
        
        self.__pcharge = pcharge
        self.__lcharge = lcharge
        self.__tcharge = tcharge

    def get_parts_charges(self):
        return self.__pcharge
    
    def get_labor_charge(self):
        return self.__lcharge
    
    def get_total_charge(self):
        return self.__tcharge

    def print_person(self):
        print(' Service Quote')
        print(f" Parts: {self.__pcharge}")
        print(f" Labor: {self.__lcharge}")
        print(f" Total Charges: {self.__tcharge}")
        