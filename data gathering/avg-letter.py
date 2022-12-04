file = open("nodups-jokes.txt", "r")

counter = 0

for x in file:
    counter = counter + len(x)

avg = counter / 200

print(avg)