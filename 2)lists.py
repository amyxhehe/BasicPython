#Module 1
continents = ["Asia","Africa","North America","South America","Australia","Antarctica","Europe"]
print(continents)

#Module 2
cat_breeds = ["british shorthair","persian","ragdoll","scottish fold"]
print(cat_breeds[2])

#Module 3
dog_breeds = ["pomeranian","husky","poodle","labrador"]
print(dog_breeds[-3])

#Module 4
baking_items = ["self-raising flour","chocolate chips","granulated sugar","cinnamon","vanilla extract"]
for item in baking_items:
    print(item)

#Module 5
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

#Module 6
cubes = [i**3 for i in range(1,11)]
print(cubes)
print(cubes[:3])

#Module 7
fruits = ['apple','banana','cherry','durian']
fruit_copy = fruits[:]
print(fruit_copy)

#Module 8
lst = [1,'two',3]
lst[1] = 2
lst.append('four')
print(lst)