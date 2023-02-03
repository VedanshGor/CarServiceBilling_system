class Car:
    def __init__(self, car_model):
        self.car_model = car_model

class Hatchback(Car):
    pass

class Sedan(Car):
    pass

class SUV(Car):
    pass

services = {
    "BS01": {"Hatchback": 2000, "Sedan": 4000, "SUV": 5000},
    "EF01": {"Hatchback": 5000, "Sedan": 8000, "SUV": 10000},
    "CF01": {"Hatchback": 2000, "Sedan": 4000, "SUV": 6000},
    "BF01": {"Hatchback": 1000, "Sedan": 1500, "SUV": 2500},
    "GF01": {"Hatchback": 3000, "Sedan": 6000, "SUV": 8000},
}

def generate_bill(car, service_codes):
    total_amount = 0
    bill = []
    for service_code in service_codes:
        service_price = services[service_code][car.car_model]
        bill.append((service_code, service_price))
        total_amount =total_amount + service_price

    if total_amount >= 10000:
        bill.append(("Complimentary Cleaning", 0))

    return bill, total_amount

if __name__ == "__main__":
    car_model=  input("Enter the car type (Hatchback, Sedan, SUV): ")
    
    
    car = eval(car_model)(car_model)
  

    service_codes = input('''\n 
                             Basic Servicing ==> BS01 \n
                             Engine Fixing   ==> EF01 \n
                             Clutch Fixing   ==> CF01 \n
                             Brake Fixing    ==> BF01 \n
                             Gear Fixing     ==> GF01 \n
                          '''
                          "Enter the service codes separated by commas:"
                          ).strip().split(",")

    bill, total_amount = generate_bill(car, service_codes)
    print("SIR , YOUR Bill IS:")
    for service, price in bill:
        print(f"{service}: ₹{price}")
    print(f"Total Amount: ₹{total_amount}")
