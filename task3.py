from task2 import Student


Danil = Student('Danil', 21, 69, 180, True, 2, 'white', 150, 4, 'Math', 9)
Grisha = Student('Grisha', 21, 69, 165, True, 2, 'white', 150, 4, 'IT', 10)


print(f'Count of Danil homeworks > count of Grisha homeworks: {Danil>Grisha}')
print(f'Count of Danil homeworks < count of Grisha homeworks: {Danil<Grisha}')
print(f'Count of Danil homeworks = count of Grisha homeworks: {Danil==Grisha}')
print(f'Count of Danil homeworks != count of Grisha homeworks: {Danil!=Grisha}')
print(f'Count of Danil homeworks >= count of Grisha homeworks: {Danil>=Grisha}')
print(f'Count of Danil homeworks <= count of Grisha homeworks: {Danil<=Grisha}')