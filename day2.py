with open('files/input.txt') as file:
    data = file.readlines()

data = [line.strip().split("\t") for line in data]


def partOne():
    checkSum = 0
    numbers = []
    for x in data:
        temp = list(map(int, x))
        temp.sort()
        numbers.append(temp[len(temp) - 1] - temp[0])
    for i in numbers:
        checkSum += i

    return checkSum

def partTwo():
    numbers = []
    checkSum = 0
    for x in data:
        temp = list(map(int, x))
        temp.sort()
        numbers.append(temp)
    print(numbers)
    for x in numbers:
        for i in range(len(x)):
            for j in range(len(x)):
                if j != i and x[j] % x[i] == 0:
                    checkSum += x[j]//x[i]
    return checkSum


print(partTwo())

