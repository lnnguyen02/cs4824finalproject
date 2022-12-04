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
    while len(string1) < len(string2):
        string1.append("")
    while len(string2) < len(string1):
        string2.append("")
    
    similarity = 0
    for x in range(len(string1)):
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

NEIGHBORS = 1


startingWords = []
for x in words:
    if KNN_classifier(x, train_data, train_labels, NEIGHBORS, dist=dist) == "J":
        startingWords.append(x)

file = open("starting-words.txt", "w")

for x in startingWords:
    file.write(x)
    file.write("\n")