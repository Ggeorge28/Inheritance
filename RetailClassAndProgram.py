# This program creates the class file and the program file together
# NOTE: wherever you see 'xxxx', that means there is code missing and
# is to be completed by you.


#Class definition (part 1) 

class RetailItem():
    def __init__(self,item1,item2,item3):
        self.__desc = item1
        self.__units = item2
        self.__price = item3

    def get_desc(self):
        return self.__desc
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price

    def set_desc(self, desc):
        self.__desc = desc
    
    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price 


    def print_retail(self):
        print("|Description|", "|Units in Inventory|", "|Price|")
        print(RetailItem.get_desc(self))
        print(RetailItem.get_units(self))
        print(RetailItem.get_price(self))



# program (part 2)
#import RetailClassAndProgram as p

# create instances
item1 = ('Jacket', 12, '$59.95')
item2 = ('Designer Jeans', 40, '$34.95')
item3 = ('Shirt', 20, '$24.95')

desc = RetailItem(item1, item2, item3)



# print out desc and price

desc.print_retail()

        



    
