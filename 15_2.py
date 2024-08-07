class Transport:

   def __init__(self, name, max_speed, mileage):

    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

class Autbus(Transport):
    def __str__(self) -> str:
       return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"
    
    def seating_capacity(self, capacity = 50):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"
test = Autbus("Renaul Logan", 200, 20)
print(test.seating_capacity())