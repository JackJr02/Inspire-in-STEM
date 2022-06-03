#Create a Vehicle Class without any variables and methods
#Include Maximum Speed and Mileage as Instances
#Print Maximum Speed and Mileage

class Vehicle:
    def __init__(instance,_speed, _mileage):
        instance.speed=_speed
        instance.mileage=_mileage
    def sayHello(instance):
        print("The maximum speed is " + str(instance.speed) + "and the mileage is " + str(instance.mileage))
vehicle=Vehicle('260Km/h ',10000)
vehicle.sayHello()
