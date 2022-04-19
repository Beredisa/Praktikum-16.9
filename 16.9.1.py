class Rec_3:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return f'Координата x = {self.x}, Координата y = {self.y},' \
               f' Ширина прямоугольника = {self.width}, Высота прямоугольника = {self.height}'

rectan = Rec_3(4, 6, 24, 92)

print(f"Результат : {rectan.get_area()}")
