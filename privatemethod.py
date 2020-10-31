class car:
    def __init__(self,speed,color):
        self.__set_speed(speed)
        self.__set_color(color)
        pass
    def __set_speed(self,speed):
        self.__speed=speed
    def get_speed(self):
        return self.__speed
    def __set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color
ford = car(30,'red')
honda=car(50,'Purple')
audi = car(80,'White')
ford=car(200,'PINK')
# this is not allowed

# ford.__set_speed(30) # SORRRRYYY NOT ALLOWWED
print(ford.get_speed())
print(honda.get_speed())
print(audi.get_speed())
print(ford.get_color())
print(honda.get_color())
print(audi.get_color())