import string
'''
file = open("knock-knock.txt", "r")

writer = open("stripped-jokes.txt", "w")

for x in file:
    if len(x) > 2:
        #joke = x.split(" ", 1)
        stripped = x.translate(str.maketrans('', '', string.punctuation))
        final = stripped.lower()
        writer.write(final)

file.close()
writer.close()
'''

file = open("not-jokes.txt", "r")

writer = open("filtered-script.txt", "w")

for x in file:
    if len(x.strip()) > 2:
        #x = x.split(".",1)[1]
        stripped = x.translate(str.maketrans('', '', string.punctuation))
        final = stripped.lower()
        writer.write(final)

file.close()
writer.close()
