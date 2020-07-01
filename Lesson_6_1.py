import time
from turtle import *

t = Turtle()
coord = [(0, 50), (0, 0), (0, -50)]
delay_light = (7, 2, 3)


def black_light():
    for i in coord:
        t.goto(i)
        t.dot(50, 'black')


class TrafficLight:
    count = 0

    def __init__(self, tl_color=('red', 'yellow', 'green')):
        self.__tl_color = tl_color

    def running(self):
        black_light()
        t.hideturtle()
        t.goto(coord[TrafficLight.count])
        t.dot(50, self.__tl_color[TrafficLight.count])
        time.sleep(delay_light[TrafficLight.count])
        if TrafficLight.count < 2:
            TrafficLight.count += 1
        else:
            TrafficLight.count = 0
        t.reset()


r = 5
print(f'Количество переключений светофора = {r}')

my_tl = TrafficLight()
black_light()
for _ in range(r):
    my_tl.running()

print("Спасибо!")
