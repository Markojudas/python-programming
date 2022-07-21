lst = [1,2,3,5,6,7,8,9,10]

listOfEvenNums = filter(lambda x: x % 2 == 0, lst)

print(list(listOfEvenNums))