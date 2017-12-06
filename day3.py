def partOne(number):
    counter = 0
    midPoints = []
    prevMax = 1
    steps = 0
    while (True):
        if number == 1:
            break
        if number in range(prevMax, (8 * counter) + 1 + prevMax):
            midPoints.append(prevMax + counter)  # Right
            midPoints.append(prevMax + (counter * 3))  # Up
            midPoints.append(prevMax + (counter * 5))  # Left
            midPoints.append(prevMax + (counter * 7))  # Down
            break
        prevMax += (8 * counter)
        counter += 1

    shortest = -1
    for i in midPoints:
        if shortest == -1:
            shortest = abs(number - i)
        else:
            if abs(number - i) < shortest: shortest = abs(number - i)
        steps = shortest + counter

    return steps



print(partOne(325489))
