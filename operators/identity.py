car = ["passat", "golf"]
car2 = ["passat", "golf"]
car3 = car
car4 = ["arteon", "golf"]

print(car is car3) #True
print(car3 is car4) #False
print(car is not car2) #True

print(car == car2)  #True
print(car is car2)  #False

