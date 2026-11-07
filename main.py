from abc import ABC, abstractmethod

# 1. Абстрактный класс (интерфейс)
class Pet(ABC):
    @abstractmethod
    def get_nickname(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def get_age_in_human_years(self):
        pass

    @abstractmethod
    def express(self):
        pass

# 2. Класс Попугай
class Parrot(Pet):
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_age_in_human_years(self):
        return int(self.age * 5) 

    def express(self):
        print(f'{self.nickname}: "Hello!"')
        print(r"""   \
   (o>
\_//)
 \_/_) 
  _|_""")

# 3. Класс Черепаха
class Turtle(Pet):
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_age_in_human_years(self):
        return int(self.age * 5.25)

    def express(self):
        print(r"""  _____     ____
 /      \  |  o |
|        |/ ___\|
|_________/
|_|_| |_|_|""")

# 4. Класс Человек
class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet

    def get_pet_info(self):
        print("--------------------")
        if self.pet is None:
            print(f"{self.name} has no pet yet")
        else:
            print(f"Pet for {self.name} is named {self.pet.get_nickname()}")
            print(f"Age: {self.pet.get_age()} year(s), about {self.pet.get_age_in_human_years()} human years")
            print("And it expresses itself like this:")
            self.pet.express()
        print("--------------------")

# 5. Основная программа
if __name__ == "__main__":
    kesha = Parrot("Kesha", 3)
    zavala = Turtle("Zavala", 4)

    jack = Person("Jack", kesha)
    john_empty = Person("John")
    john_with_pet = Person("John", zavala)

    jack.get_pet_info()
    john_empty.get_pet_info()
    john_with_pet.get_pet_info()