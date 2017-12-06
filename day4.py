with open('files/day4.txt') as file:
    data = file.readlines()

data = [line.strip().split(" ") for line in data]

def partOne(data):
    counter = 0
    for i in data:
        if len(i) == len(set(i)) : counter += 1  #Passphrase is the same length as a set of itself, then there are no repeat words
    return counter

def partTwo(data):
    counter = 0
    for i in data:
        tempArr = []
        for x in i:
            tempArr.append(''.join(sorted(x)))  # Sorting the strings, since anagrams would be similar if they are sorted

        if len(i) == len(set(tempArr)) : counter +=1
    return counter


print(partTwo(data))

