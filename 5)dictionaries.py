#Module 1
cat = {"color":"orange","age":5}
print(cat)
print("The color of the cat is:" + cat["color"])


#Module 2
ages = {"Amy":19, "Carol":29}
for i in ages:
    print("{} is {} years old.".format(i,ages[i]))


#Module 3
capitals = {}
capitals["South Korea"] = "Busan"
capitals["Pakistan"] = "Islamabad"

capitals["South Korea"] = "Seoul"

print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())


#Module 4
users = []

user1 = {
    'last': 'carlo',
    'first': 'santiago',
    'username': 'carlo_s',
 }
users.append(user1)

user2 = {
    'last': 'john',
    'first': 'edgerton',
    'username': 'johnEd',
 }
users.append(user2)

for user in users:
    for k, v in user.items():
        print(k + ": " + v)
    print("\n")


#Module 5
fav_foods = {'jen': ['burrito', 'pizza'], 'sarah': ['cake'], 'edward': ['spaghetti', 'popcorn']}
for name, foods in fav_foods.items():
    print(name + ": ")
    for food in foods:
        print("- " + food)


#Module 6
doggos = []

for doggo_num in range(100):
    new_doggo = {}
    new_doggo['color'] = 'golden'
    new_doggo['points'] = 5
    new_doggo['x'] = 20 * doggo_num
    new_doggo['y'] = 7 * int(new_doggo['x'])
    doggos.append(new_doggo)

num_doggos = len(doggos)
print("Number of doggos created:")
print(num_doggos)