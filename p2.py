from difflib import SequenceMatcher

file1 = open("nodups-jokes.txt", "r")
file2 = open("filtered-script.txt", "r")
file3 = open("words.txt", "r")

train_data = []
train_labels = []
words = []

for x in file1:
    train_data.append(x.strip())
    train_labels.append("J") #J FOR JOKE

for x in file2:
    train_data.append(x.strip())
    train_labels.append("N") #N FOR NOT JOKE

for x in file3:
    words.append(x.strip())

file1.close()
file2.close()
file3.close()


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def dist(curr , string):
    string1 = curr.split(" ")
    string2 = string.split(" ")
    
    similarity = 0
    for x in range(min(len(string1), len(string2))):
        similarity = similarity + similar(string1[x], string2[x])
    return similarity


def find_KNN(x, train_data, train_labels, K, dist=dist):
    arr = []
    for i in range(len(train_data)):
        if len(arr) < K:
            temp = [dist(x,train_data[i]),i]
            arr.append(temp)
            arr.sort()
        else:
            distance = dist(x,train_data[i])
            temp = [distance, i]
            arr.append(temp)
            arr.sort()
            arr.pop(0)
                       
    arrAnswer = []
    for i in range(K):
        arrAnswer.append(arr[i][1])
    return arrAnswer

def KNN_classifier(x, train_data, train_labels,K,dist=dist):
    arr = find_KNN(x, train_data, train_labels, K, dist)
    labels = []
    for i in arr:
        label = train_labels[i]
        labels.append(label)

    maxValue = max(set(labels), key = labels.count)
    return maxValue
    ##### END OF CODE #####

file = open("starting-words.txt", "r")

starting = []

for x in file:
    starting.append(x.strip())

avg = []
for x in range(len(starting)):
    curravg = 0
    for j in range(200):
        curravg = curravg + dist(starting[x], train_data[j])
    curravg = curravg / 200
    avg.append(curravg)

startingword = starting[avg.index(max(avg))]
print(startingword)


#Second Iteration
nextphrase = startingword
for m in range(11):
    next = []

    for x in range(len(words)):
        string = nextphrase.strip() + " " + words[x].strip()
        next.append(string)

    simscore = []
    for x in next:
        currscore = 0
        for j in train_data[0:200]:
            currscore = currscore + dist(x, j)
        currscore = currscore / 200
        simscore.append(currscore)

    nextphrase = next[simscore.index(max(simscore))]
    print(nextphrase)