class Person:
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


    def print_person(self):
        print(f" Name :", self.__name)
        print(f" Address:", self.__address)
        print(f" Phone:", self.__phone)



class Customer(Person):

    def __init__(self,name,address,phone,customer_number,mailing_list):

        Person.__init__(self,name,address,phone)

        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    

    def print_person(self):
        print(" Name:", Person.get_name(self))
        print(" Address:", Person.get_address(self))
        print(" Phone:", Person.get_phone_number(self))
        print(f" Customer Number: {self.__customer_number}")
        #print(f" Mailing List: {self.__mailing_list}")
        if self.__mailing_list:
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")