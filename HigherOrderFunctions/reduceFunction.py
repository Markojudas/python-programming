from functools import reduce

lst = [1,2,3,4,5]

sumList = reduce(lambda x, y: x * y, lst)

print(sumList) #15
