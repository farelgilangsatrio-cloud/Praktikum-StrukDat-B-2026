class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

# ubah properti
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
print(p1.age)

# hapus item
def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("Linus", 18)
del p1.age
print(p1.name)
print(p1.age)
