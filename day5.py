with open('files/day5.txt') as file:
    data = file.readlines()

data = [int(line.strip()) for line in data]

def partOne():
    counter = 0
    steps = 0
    while True:
        if counter >= len(data):
            break
        temp = data[counter]
        data[counter] = data[counter] + 1
        counter += temp
        steps += 1
    return steps

def partTwo():
    counter = 0
    steps = 0
    while True:
        if counter >= len(data):
            break
        temp = data[counter]
        if temp >= 3: data[counter] = data[counter] - 1
        else: data[counter] = data[counter] + 1
        counter += temp
        steps += 1
    return steps


print(partTwo())