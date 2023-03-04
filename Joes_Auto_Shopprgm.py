import Joeautoshop as p

name = 'John Doe'
address = '123 Main St. Waco TX 76706'
phone = '214-555-1112'
make = 'Honda'
model = 'Accord LX'
year = '2016'
pcharge = '$1,210.50'
lcharge = '$765.00'
tcharge = '$2,138.48'

person1 = p.Customer(name,address,phone)

Car = p.Car(name,address,phone,make,model,year)

Service = p.Service(pcharge,lcharge,tcharge)

#person1.print_person()

Car.print_person()
Service.print_person()