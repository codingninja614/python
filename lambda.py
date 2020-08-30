from functools import reduce
my_list=[1,2,3,4,5]
print(list(map(lambda item: item*2,my_list)))
print(reduce(lambda acc,item:acc+item,my_list))
print(list(filter(lambda item:item%2!=0,my_list)))

#lambda exercise
#question1 squaring list elements
list1=[1,2,3,4]
print(list(map(lambda item: item*item,list1)))

#qestion2 sorting
a=[(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)
