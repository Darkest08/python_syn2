class Turtule:
    
    def __init__(self, x = 0, y = 0, s = 1):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y-=self.s

    def go_down(self):
        self.y+=self.s

    def go_left(self):
        self.x-=self.s

    def go_right(self):
        self.x+=self.s

    def evolve(self):
        self.s+=1

    def degrade(self):
        if self.s > 0:
            self.s-=1
        else:
            print("Ошибка! Скорость не может упасть ниже 0")

    def count_moves(self, x2, y2):
        return int(abs(x2 - self.x) / self.s + abs(y2 - self.y) / self.s)

test = Turtule(0, 0, 1)
test.degrade()
test.degrade()
test.evolve()
test.go_left()
test.go_left()
print(test.count_moves(0,0))