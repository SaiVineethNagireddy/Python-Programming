#Polymorphism

#class polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()
print()

#Inheritance Class Polymorphism
class human:
  def __init__(self, phase, status):
    self.phase = phase
    self.status = status

  def move(self):
    print("Move!")

class old(human):
  pass

class Adult(human):
  def move(self):
    print("Run!")

class infant(human):
  def move(self):
    print("Crawl!")

OLD = old("oldage", "married")
ADULT = Adult("teen", "may or may not")
INFANT = infant("child", "no")

for x in (OLD, ADULT, INFANT):
  print(x.phase)
  print(x.status)
  x.move()
print() 