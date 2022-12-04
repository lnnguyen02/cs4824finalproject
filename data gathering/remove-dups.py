file = open("stripped-jokes.txt", "r")

writer = open("nodups-jokes.txt", "w")

arr = []

for x in file:
    if x not in arr:
        arr.append(x)

for x in arr:
    writer.write(x)

print(len(arr))

file.close()

writer.close()