class Car:

    def __init__(self, speed, color='black', name="Машинка", is_police=False):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = is_police

    def go(self, accelerat=1):
        self.speed = self.speed + accelerat * 10
        print(f"Поехали")

    def stop(self, accelerat=-1):
        self.speed = self.speed + accelerat * 10
        if self.speed < 0:
            self.speed = 0
        print(f"Тормозим")

    def turn(self, direction):
        print(f"Поворот на {direction} на скорости {self.speed} ", end='')
        if self.speed > 80:
            print(f"Очень опасная скорость для поворота")
        else:
            print("\n")

    def show_speed(self):
        print(f"Cкорость = {self.speed}")
        if self.is_police and self.speed > 90:
            print(
                f" ВНИМАНИЕ! PoliceCar может разгоняться до скорости превышающей 90 может только преследуя нарушителя!")
        else:
            print("\n")


class TownCar(Car):

    def show_speed(self):
        print(f"Cкорость = {self.speed}", end='') if self.speed > 0 else print(f"стоим")
        if self.speed > 60:
            print(f" ВНИМАНИЕ! Превышение скорости для TownCar")
        else:
            print("\n")


class WorkCar(Car):

    def show_speed(self):
        print(f"Cкорость = {self.speed}", end='') if self.speed > 0 else print(f"стоим")
        if self.speed > 40:
            print(f" ВНИМАНИЕ! Превышение скорости для WorkCar")
        else:
            print("\n")


class SportCar(Car):
    def show_speed(self):
        print(f"Cкорость = {self.speed}", end='') if self.speed > 0 else print(f"стоим")
        if self.speed > 150:
            print(
                f" ВНИМАНИЕ! SportCar может разгоняться до скорости превышающей 150 может только на спортивном треке!")
        else:
            print("\n")


class PoliceCar(Car):
    def __init__(self, speed, is_police):
        self.speed = speed
        self.is_police = is_police


def go_cars(cars, rounds=2, step=2):
    for i in range(rounds):
        print(f'----***---- {i + 1}-й круг для {type(cars)} ----***---- ')
        cars.go(step)
        cars.show_speed()
        cars.go(3 * step)
        cars.show_speed()
        cars.stop(-step * 2)
        cars.turn("лево")
        cars.stop(-step)
        cars.show_speed()
        cars.turn("право")
        cars.stop(-step * 2)
        cars.show_speed()


if not input('Стартуем TownCar? '):
    my_car = TownCar(4)
    go_cars(my_car, 3, 3)

if not input('Стартуем WorkCar? '):
    my_car = WorkCar(3)
    go_cars(my_car, 4, 2)

if not input('Стартуем SportCar? '):
    my_car = SportCar(7)
    go_cars(my_car, 2, 10)

if not input('Стартуем PoliceCar? '):
    my_car = PoliceCar(6, True)
    go_cars(my_car, 1, 6)
