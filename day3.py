def findLocation(number):
    counter = 0
    prevMax = 0
    while(True):
        if number in range(prevMax, (8 * counter) + 1 + prevMax):
                break
        prevMax = (8*counter)+1
        counter += 1
    return counter


print(findLocation(325489))
