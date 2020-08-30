#list,set comprehension
my_list=[char for char in "Hello World"]
my_list2=[num for num in range(0,100)]
my_list3=[num**2 for num in range(1,11)]
my_list4=[num**2 for num in range(1,11) if num%2==0]     #list=[param for param in iterable condition]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

#dictionary comprehension
simple_dict={
"a":1,
"b":2
}
my_dict={k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict)


my_dict1={num:num*2 for num in [1,2,3,4,5]}
print(my_dict1)

some_list=["a","b","c",'b',"d","m","n","n"]
duplicate=list(set(x for x in some_list if some_list.count(x)>1 ))
print(duplicate)

list5=[1,2,3,4,5]
my_list5=[item**3 for item in list5 if item>2]
print(my_list5)
