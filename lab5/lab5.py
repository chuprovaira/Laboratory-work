#1
class Book:
    def __init__(self, title, autor, year):
        self.title = title
        self.autor = autor
        self.year = year

    def get_info(self):
        return f'Name book:{self.title} , Name autor: {self.autor} , Year of publication: {self.year}'

check=Book('Преступление и наказание', 'Федор Михайлович Достоевский' , '1866')
print(check.get_info())

#2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return f'Radius value: {self.radius}'
    def set_radius(self, new_radius):
        self.radius = new_radius

ball = Circle(15)
print(ball.get_radius() , ball.set_radius(12) , ball.get_radius())
