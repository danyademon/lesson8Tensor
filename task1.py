class Animals():
    def __init__(self,name,age,weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

class Mammals(Animals):
    def __init__(self, name, age, weight, height, IsWool, legs_count, color):
        super().__init__(name, age, weight, height)
        self.IsWool = IsWool
        self.legs_count = legs_count
        self.color = color
    
class Human(Mammals):
    def __init__(self, name, age, weight, height, IsWool, legs_count, color, iq):
        super().__init__(name, age, weight, height, IsWool, legs_count, color)
        self.iq = iq
    
    def say(self):
        print(f'Ma name is {self.name}. I am human.')

class Cat(Mammals):
    def __init__(self, name, age, weight, height, IsWool, legs_count, color):
        super().__init__(name, age, weight, height, IsWool, legs_count, color)

    def say(self):
        print('Meow')

class Dog(Mammals):
    def __init__(self, name, age, weight, height, IsWool, legs_count, color):
        super().__init__(name, age, weight, height, IsWool, legs_count, color)
        
    def say(self):
        print('Bark')

if __name__ == '__main__':
    Tom = Human('Tom', 23, 69, 180, True, 2, 'white', 150)
    Kitty = Cat('Kitty', 3, 15, 40, True, 4, 'black')
    Doggy = Dog('Doggy', 5, 30, 50, False, 4, 'grey')

    for mammals in (Tom, Kitty, Doggy):
        mammals.say()