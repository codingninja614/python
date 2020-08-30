#Numbers basics
print(2+4)
print(2**3)          #it gives us exponential
print(2*3)
print(2/4)
print(8%5)          #it gives us remainder
print(type(2/4))
print(6//4)    
print(round(3.4))  #just rounds off a number
print(round(8.9))
print(abs(-77))    #gives absolute value of a number
print(bin(5))    #gives binary equivalent of a decimal number
print(int('0b1010',2))   #int(number,base)
a=10             #expression 
user_age=a/2     #statement
print(user_age)
a*=20           #augmented assignment operator
print(a)    


# string basics
s1="Hiii Elizabeth"
d="12345u6764"
print(d.isdigit())
print(s1.islower())
print(type('I am Sameer Malik'))
long_string='''
W O W                       
 00
_ _ _
'''
print(long_string)      # multiline strings
first_name="Sameer"
last_name=" malik"
full_name=first_name +last_name    #string concatenation
print(full_name)
print('hello'+ ' sameer')
print('hello'+' '+ str(5))
print(type(int(str(100))))
weather="It\'s \"kind of\" \"sunny\""
print(weather)
b='It\'s \"just\" I \"hate\" coding.'
print(b)
c='It\'s \"just\" I \"hate\" \n coding.'  #to go to next line
d='It\'s \"just\" I \"hate\" \t coding.'  #to add 1 tab space
print(c)
print(d)



#formated string
name="Sameer_Malik"
age=20
greeting="Good morning"
print(f"Hi {name}, {greeting}. Your age is {age} years old.")
print("Hi {} your age is {} years old.".format(age,name))
print("Hi {} your age is {} years old.".format("Sameer",55))



# String indexes
selfish="012345678"
print(selfish[:9:2])
print("hi")
print(len(selfish))
print(selfish[0:len(selfish)])
phrase="i am inevitable"
print(phrase.capitalize())
print(phrase.casefold())
print(phrase.upper())
print(phrase.find("am"))
print(phrase.replace("am","are"))
print(phrase)
e=5
e=7
print(e)
print(e)


#booleans
print(bool(1))
print(bool(0))

#Calculating age exercise
name=input("Enter your name:")
DOB=int(input("Enter your year of birth:"))
age=2020-DOB
a=len(name)
print(f"Hey {name},you are {age} years old and your name is {a-1} characters long.")


#password checker exercise
username=input("Enter your username:")
password=input("Enter your password:")
a=len(password)
print(f"Hey {username}, your password {a*'*'} is {a} characters long.")



#loops pattern
n=int(input("Enter no of rows:"))
for i in range(n):
  print(str(n)*n)
n=int(input("Enter no of rows:"))
for i in range(n):
  print((chr(65+i)+' ')*(i+1))
n=int(input("Enter no of rows:"))
for i in range(n):
  print('* '*(n-i))
n=int(input("Enter no of rows:"))
for i in range(n):
  for j in range(n-i):
    print(j+1,end=' ')
  print()
n=int(input("Enter no of rows:"))
for i in range(n):
  for j in range(n-i):
    print((n-j),end=' ')
  print()
n=int(input("Enter no of rows:"))
for i in range(n):
  print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
n=int(input("Enter no of rows:"))
for i in range(n):
  print(' '*(n-i-1),end='')
  for j in range(i+1):
    print(chr(64+n-j),end=' ')
  print()  
n=int(input("Enter no of rows:"))
for i in range(n):
  for j in range(i+1):
    print(chr(65+j),end=' ')
  print()  
for i in range(n-1):
  for j in range(n-i-1):
    print(chr(65+j),end=' ')
  print()

n=int(input("Enter no of rows:"))  
for i in range(n):
  print(" "*(n-i-1)+ (" " +"*")*(i+1))
for i in range(n-1):
  print(" "*(i+1)+ (" " +"*")*(n-i-1))
print() 

#lists
e_cart=["Sunglasses","Chocolates","toys","notebooks"]
print(e_cart[0:len(e_cart)])
e_cart[3]="laptop"
print(e_cart)        #it shows the mutability of lists
matrix=[
[1,2,3,4],
[2,4,6,8],
[3,6,9,12]
]
print(matrix[1][3])
#print(matrix[1][4])      *index error


#list methods
basket=[9,1,2,3,8,4,5,6,6]
print(len(basket))
basket1=basket
basket1.pop(3)      #removes the no present on index given
basket1.remove(5)   #removes the no given
basket1.append(7)   #adds a no at the last
print(basket1.count(6))  #counts the no of passed items
print(basket1.sort())     #sorts a list
print(basket1.reverse())     #reverses the sequence of items
print(list(range(1,101)))
sentence=" "
sentence1=sentence.join(["hi","sameer","how","are","you"])
print(sentence1)
print(basket1)
a,b,c, *others,d=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(others)



#dictionary
dictionary={
  "a":[1,2,3,4,5,6],
  "b":"hello",
  "c":True
}
print(dictionary["a"][4])
print(dictionary["b"])
my_list=[
{
"a":[1,2,3,4,5,6],
"b":"hello",
"c":True
},
{
  "a":[2,4,6,8,10,12],
  "b":"hiiii",
  "c":False
}
]
print(my_list[1]["a"][5])
          #0r
print(dictionary["a"][4])    



#dictionary methods
print(dictionary.get("age"))
print(dictionary.get("age",60))     #default value is set 60
print("a" in dictionary.keys())
print([1,2,6,5,4,3] in dictionary.values())
print(dictionary.items())
dict=dictionary.copy()
print(dict)
print(dict.pop("a"))
print(dictionary.popitem())
print(dictionary.items())
dictionary.update({"c":False})
print(dictionary.items())



#set    
my_set={0,1,1,2,3,4,5,6}
your_set={5,6,7,8,9,10}
print(my_set)
print(len(my_set))
print(my_set.difference(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.intersection(your_set))
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(my_set.union(your_set))
print(my_set.difference_update(your_set))
print(my_set)



#extra efforts
is_old=int(input("Enter your current age:"))
if is_old>60 and is_old<=120:
  print("You are too old to drive!")
elif is_old>120:
  print('It\'s time to die buddy')  
else:
  print("Young guy enjoy your ride")  


is_licenced=input('''Do you have licence:
yes
no
''')


if is_licenced=="yes":
  print("You can drive now!")
elif is_licenced=="no":
    print("Get yourself a licence please!")
else:
  print("Please answer the question asked in yes or no only!")  
  


#conditional logic
number=int(input("Enter a number of your choice:"))
if number%2==0:
  print("Number is even!")
else:
  print("Number is odd!")  
 
#Truthy and Falsy
is_old="Hello"
is_licenced="gfhjhk"
if is_old and is_licenced:
  print("You are old enough to drive,you have a licence!!")
else:
  print("You are not of age!!")   


#logical operators
print(7>6)
print("a">"b")
print("a">"A")
print(1<2<3<4>5)
print(1<2<3<4<5)
print(0!=0)
print(not(True))
is_magician=False
is_expert=True
if is_magician and is_expert:
  print("You are a master magician!!")
elif is_magician and not(is_expert):
  print("Atleast you are getting!!")  
elif not(is_magician):  
  print("You need magical powers!!")



#is v/s ==
print(True==1)            
print(' '==1)  
print([]==1)
print(10==10.0)
print([]==[])
print(True is 1)
print(' ' is 1)  
print([] is 1)
print(10 is 10.0)
print([] is [])



#for loops
for item in (1,2,3,4,5,6):
  print(item)
  print(item)
print(item)  
for item in (1,2,3,4,5,6):
  for x in ["a","b","c"]:
    print(item,x)



#Iterables
user={
  "name":"golem",
  "age":5006,
  "can_swim":False
}
for items in user.items():
  print(items)
for i in user.values():
  print(i)
for i in user.keys():
  print(i)    


#exercise:Tricky counter
my_list=[1,2,3,4,5,6,7,8,9,10]
counter=0
for x in my_list:
  counter+=x
print(counter) 


#range
for i in range(10):
  print(i)
for a in range(0,11,2):
  print(a)
for b in range(10,0,-2):
  print(b)  
for _ in range(3):
  print(list(range(10)))  



#while loops
i=0
while i<5:
  print(i)
  i+=1
else:
  print("done!")  
while True:
  response=input("Say something!") 
  if (response=="bye"):
    break
my_list=[1,2,3,4,5,6] 
for i in my_list:
  pass
i=0
while i<len(my_list):
  i+=1
  continue
  print(my_list)  


#our first GUI
picture=[
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
  ]
for i in picture:
  for j in i:
    if j==1:
      print("*",end="")
    else:
      print(" ",end="") 
  print('')     


#exercise:Duplicate
list1=[1,2,2,3,4,4,5,6]  
duplicate=[]
for i in list1:
  if list1.count(i)>1:
    if i not in duplicate:
      duplicate.append(i)
print(duplicate)    



#functions
def say_hello():    #function defining
  print("HELLO")
  print("SAMEER")
  print("HOW")
  print("ARE")
  print("YOU")
say_hello()          #function calling
say_hello()  

def user(name="Ironman",age=52):
  print(f"helloooo {age} years old {name}!!")
user("Sameer",21)  
user("Apala",20)
user(100,"Poorvi")        #positional arguments
user()
user(age=69,name="samantha saints")    #keyword arguments

#*args ans **kwargs
def sum(*args,**kwargs):
  sum=0
  sum1=0
  for item in args:
    sum+=item
  for item in kwargs.values():
    sum1+=item  
  total=sum+sum1
  return total 
print(sum(1,2,3,6,num1=4,num2=5,no=8))
#here things like "name" and "age" are parameters and things like "sameer",21,20,69,"apala","poorvi" these are arguments to the above mentioned parameters 


#return keyword
def sum(num1,num2):
  return num1+num2
print(sum(10,40))  

def sum(num1,num2):
  return num1+num2
total=sum(100,200)
print(sum(20,total))

#docstrings
def test(a):
  '''Info:this function tests and prints parameter a'''
  print(a)
test("!!!")
#test()
     #or
help(test)
     #or
print(test.__doc__)     
  

#exercise function
def highest_even(list):
  even=[]
  for i in list:
    if i%2==0:
      even.append(i)
  return max(even)
print(highest_even([1,3,2,66,33,87,67,88]))      

#scope
if True:
  x=10
def some_func():
  total=100
  return total
  print(total) 
print(x)

if True:
  x=10
def some_func():
  total=100
  return total
  print(total) 
print(x)
print(some_func())


#global keyword
total=0
def count():
  total=0
  total+=1
  return total
count()
count()
print(count())

total=0
def count():
  global total      #use of global keyword
  total+=1
  return total
count()
count()
print(count())  
      #or
total=0
def count(total):
  total+=1
  return total

print(count(count(count(total)) ) )



#non local keyword
def outer():
  x="local"
  def inner():
    nonlocal x
    x="nonlocal"
    print("Inner:",x)
  inner()
  print("Outer:",x) 
outer()   



#object oriented programming
class Animals:
  def __init__ (self,name,specie,age):
    self.name=name
    self.age=age
    self.specie=specie

  def run(self):
    print(f"{self.name} is running!")
    print(":)")
    return("\n")  

  def eat(self):
    print(f"{self.name} is eating!! :)") 
    print ("Tummy is full now")
    return("\n")
    

animal1=Animals("shadow","Doggy",5)
animal2=Animals("happy","cat",1)
print(animal1.name)
print(animal1.age)
animal1.run()
animal2.eat()
print(animal2.specie)
print(animal1)
print(animal2)
print("\n")


#attributes and methods
class PlayerCharacter:
  membership=True
  def __init__(self,name,age):
    if age>18:
      self.name=name
      self.age=age
    else:
      self.name=name
      print(f"sorry {self.name} you cant play as this game is only for 18+:(")  
      self.age="You are minor!!"
  def run(self):
    print("run")
    return "done"
player1=PlayerCharacter("Sameer_Malik",20)
player2=PlayerCharacter("Apala_Singh",17)
player1.run()
print(player2.name)
print(player2.age)
print("\n")


#pillars of oops

#1.Encapsulation
class PlayerCharacter:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def speak(self):
    print(f"my name is {self.name}, and i'm {self.age} years old!!")  
    return "!"
player1=PlayerCharacter("Sameer_Malik",20)
print(player1.name)
player1.age=30
print(player1.age)
player1.speak()
print("\n")


#2.Abstraction
class PlayerCharacter:
  def __init__(self,name,age):
    self._name=name
    self._age=age
  def speak(self):
    print(f"my name is {self._name}, and i'm {self.age} years old!!")  
    return "!"
player1=PlayerCharacter("Sameer_Malik",20)
print(player1._name)
player1.age=30
print(player1.age)
player1.speak()
print("\n")

#3.Inheritance
class Animals():
  def playing(self):
    print("Ready to play:)")
    print("Play with me!")

class Dog(Animals):
  def __init__(self,name,color,sex):
    self.name=name
    self.color=color
    self.sex=sex
  def barking(self) :
    print(f"{self.sex} {self.name} barks like:-Bhowww bhowww!!!")
    return ("done barking!!")
class Cat(Dog):
  def __init__(self,name,color,sex):
    self.name=name
    self.color=color
    self.sex=sex
  def shouting(self) :
    print(f"{self.sex} {self.name} shouts like:-Meowww meowww!!!")
    return ("done shouting!!")  
dog1=Dog("glow","black","female")
dog2=Dog("shadow","black","male")
cat1=Cat("happy","brown","female")
dog1.barking()
dog2.barking()
cat1.shouting()
dog1.playing()
cat1.playing()
print(isinstance(dog1,Dog))
print(isinstance(dog1,Animals))
print(isinstance(cat1,Dog))
print(isinstance(cat1,Animals))
print(isinstance(dog1,Cat))
cat1.barking()


#4.Polymorphism
class PlayerCharacter():
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def run(self):
    print("run!")
    return "done" 
class Wizard(PlayerCharacter):
  def __init__(self,name,powers):
    self.name=name
    self.powers=powers
  def attack(self):
    print(f"{self.name} is attacking with power of {self.powers}!")
class Archer(PlayerCharacter):
  def __init__(self,name,num_arrows):
    self.name=name
    self.num_arrows=num_arrows
  def attack(self):
    print(f"{self.name} is attacking with arrows:{self.num_arrows}")
wizard1=Wizard("Sameer",50)
archer1= Archer("Apala",100) 
wizard1.attack()
archer1.attack()
wizard1.run()
print(dir(wizard1))
print("\n")
print(dir(list))


#dunder methods
class Toy():
  def __init__(self,color,age):
    self.color=color
    self.age=age
  def __str__(self):
    return f"{self.color}"  
    print(str("hii"))
  def __len__(self):
    return 5
action_figure=Toy("red",20)
print(action_figure.__str__())   
print(str(action_figure))
print(len(action_figure))


#exercise
class SuperList(list):
  def __len__(self):
    return 1000
super_list1=SuperList()
print(len(super_list1))
super_list1.append(5)
super_list1.append(6)
super_list1.append(7)
print(super_list1[2])
print(issubclass(SuperList,list))