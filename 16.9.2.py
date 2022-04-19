class Rec_4:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return f" Площадь прямоугольника = {self.width*self.height}"

    def get_area_side(self):
        return f" Ширина прямоугольника = {self.width}, Высота прямоугольника = {self.height}"

rectan = Rec_4(24, 92)

print(f"Результат : {rectan.get_area()}")
print(f"Результат : {rectan.get_area_side()}")