#Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
#выводит информацию о животном в формате "Имя: имя, Вид: вид".

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        print(f"Имя: {self.name}, Вид: {self.species}")


animal1 = Animal("Барсик", "Кошка")
animal1.info()

animal2 = Animal("Шарик", "Собака")
animal2.info()
