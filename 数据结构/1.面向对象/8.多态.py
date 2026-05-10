class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

class Bird(Animal):
    def speak(self):
        print("叽叽喳喳")

class Car:
    def speak(self):
        print("车在跑")

def animal_speak(ab: Animal):
    ab.speak()

if __name__ == '__main__':
    d = Dog()
    c = Cat()
    b = Car()

    animal_speak(d)
    animal_speak(c)
    animal_speak(b)