class cash_register:
    def __init__(self, cash = 0):
        self._cash = cash

    def top_up(self, x):
        if x >= 0:
            self._cash+=x
    
    def count_1000(self):
        print(self._cash // 1000)

    def take_away(self, x):
        if x <= self._cash:
            self._cash-=x
        else:
            print("Ошибка! Недостаточно средств!")

test = cash_register()
test.top_up(2300)
test.count_1000()
test.take_away(3000)
test.take_away(500)