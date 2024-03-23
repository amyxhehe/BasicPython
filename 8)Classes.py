#Module 1
class Cat():
    def __init__(self, n):
        self.name = n
    def eat(self):
        print(self.name + " is eating.")

class strayCat(Cat):
    def __init__(self, n):
        super().__init__(n)
    def roam(self):
        print(self.name + " is roaming the streets.")

cat1 = Cat("Brownie")
print(cat1.name + " is a cutie pie.")
cat1.eat()

cat2 = strayCat("Ginger")
print(cat2.name + " is a stray cat.")
cat2.eat()
cat2.roam()


#Module 
class Cake():
    def __init__(self, flavor, weight):
        self.flavor = flavor
        self.weight = weight
    def bake(self):
        print("The cake is in the oven.")
    def decorate(self):
        print("The cake is being decorated.")

my_cake = Cake("Vanilla Rosemary", 2)
print("You ordered a {} cake of {}lbs.".format(my_cake.flavor, my_cake.weight))
my_cake.bake()