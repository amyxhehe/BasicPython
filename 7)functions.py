#Module 1
def function():
    print("Hello Earthlings!")
function()


#Module 2
def f(n = "Marie"):
    print("Hello " + n.capitalize() + "!")

f()
name = input("What is your name: ")
f(name)


#Module 3
def product(x = 8, y = 9):
    p = x*y
    return p

n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

print(product(n1,n2))


#Module 4
def pet_info(animal = "parrot", name = "larry"):
    print("I have a " + animal + ".")
    print("Its name is " + name.capitalize() + ".")
    print("\n")

pet_info()
pet_info('hamster', 'harry')
pet_info(animal='lion', name='Simba')
pet_info(name='willie', animal='dog')


#Module 5
def full_name(first_n,last_n):
    n = first_n.capitalize() + " " + last_n.capitalize()
    return n
name = full_name("Amy","hehe")
print(name)


#Module 6
def create_user(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person

user = create_user('jimi', 'hendrix', 27)
print(user)
user = create_user('janis', 'joplin')
print(user)