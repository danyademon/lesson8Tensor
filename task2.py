from task1 import Human

class Student(Human):
    def __init__(self, name, age, weight, height, IsWool, legs_count, color, iq, course, speciality, count_of_homeworks):
        super().__init__(name, age, weight, height, IsWool, legs_count, color, iq)
        self.course = course
        self.speciality = speciality 
        self.count_of_homeworks = count_of_homeworks
    
    def __lt__(self, other):
        x = self.count_of_homeworks
        y = other.count_of_homeworks
        return x < y

    def __le__(self, other):
        x = self.count_of_homeworks
        y = other.count_of_homeworks
        return x <= y
    
    def __eq__(self, other):
        x = self.count_of_homeworks
        y = other.count_of_homeworks
        return x == y
    
    def __ne__(self, other):
        x = self.count_of_homeworks
        y = other.count_of_homeworks
        return x != y
    
    def __gt__(self, other):
        x = self.count_of_homeworks
        y = other.count_of_homeworks
        return x > y
    
    def __ge__(self, other):
        x = self.count_of_homeworks
        y = other.count_of_homeworks
        return x >= y