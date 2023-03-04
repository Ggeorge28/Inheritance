import Exercise as p

name = 'John'
address = '1234 Main St'
phone = '123-456-7890'
Customer_number = 1234
mailing_list = True

person1 = p.Person(name,address,phone)

customer1 = p.Customer(name,address,phone,Customer_number,mailing_list)

person1.print_person()

print()
print()
print()

customer1.print_person()