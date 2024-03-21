#Module 1
colors = ["green","white","grey"]
for color in colors:
    print(color)

#Module 2
num = 50
while True:
    print(num)
    break


#Module 3
banned_users = ['eve', 'fred', 'gary', 'helen']
prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "
players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned!")
        continue
    else:
        players.append(player)
        
print("\nYour team:")
for player in players:
    print(player)


#Module 4
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'fish' in pets:
    pets.remove('fish')

print(pets)