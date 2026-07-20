#**************************************************Pyhton Notes*********************************************************
#Print Statement
print("Hello Boss")


#***********************************************************************************************************************
#Operators
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Comparison operators(=,>,<,==,!=,<=,>=)
print(10 > 5)
print(8<2)

#Logical Operators(and,or,not)
age = 20
print(age > 18 and age > 21)
print(age > 18 or age < 30)

#Assignment Operators(+=,-=,*=,/=)
x = 5
x += 2
print(x) #now x is updated as 7
x -=1
print(x) #here 1 will be subtracted fron updated x

#Membership Operators(in,not in)
Devices=["Phone","Laptop","Pods"] #List
print("Phone" in Devices)

#Identity Operators
c=[2,3]
d=c
e=[3,4]
print(c is d)
print(d is c)
print(e is d)
print(e is c) #== compares values, while is compares object identity.

#***********************************************************************************************************************


#variables
Marks=5 #int
Credit_hours=3.5 #float
Grade_points=Marks*Credit_hours
Student_name="Meer" #string
print(Grade_points)
print("Grade points of "+Student_name+" are "+str(Grade_points)) # by using data type conversion.
print(f"Grade points of {Student_name} are {Grade_points}") #by f string(merging different data types in one line)

#***********************************************************************************************************************

#Data Types

#checking data type
print(type(Credit_hours))

#type conversion
num=30
num=str(num)
print(num)
print(type(num))

#***********************************************************************************************************************
#Strings
#Indexing(0,1,2,3,4...)
Name="Meer"
print(Name[0])

#Negative Indexing(...-4,-3,-2,-1)
Name2="Heer"
print(Name2[-2])

#Slicing :General form= "text[start:stop:step]"
Name3="Meer"
print(Name3[0:2])

#String methods

#Uppercase
Name4="meer"
print(Name.upper())

#Lowercase
Name5="MEER"
print(Name5.lower())

#Replace
Name6="Meer"
print(Name6.replace("Meer","Heer"))

#Lenght
Name7="Meer"
print(len(Name7))

#Split
Sentence="Hey there!This is Meer"
print(Sentence.split())

#Join
print("!".join(["Hey","You Idiot "]))

#F-Strings
name2= "Meer"
age2 = 20
print(f"My name is {name2} and I am {age2} years old.")

#**********************************************************************************************************************
#inputs
#name=input("Enter your name:")
#print(f"Name is : {name}")
#print(type(name))

#age=int(input("Enter your age:"))
#print(f"age is : {age}")
#print(type(age))

#**********************************************************************************************************************
#Lists   (Lists are mutable)
fruits = ["Apple","Banana","Orange"]
print(fruits)
#list methods"

#Access elements
print(fruits[0])

#Replace elements
fruits[1]="Kiwi"
print(fruits)

#Add elements
fruits.append("Grapes")
print(fruits)

#Remove elements
fruits.remove("Orange")
print(fruits)

#Insert elements
fruits.insert(3,"Watermelon")
print(fruits)

#Clear list
#fruits.clear()
#print(fruits)

#Length
print(len(fruits))

#Loop
for fruit in fruits:
    print(fruit)

#***********************************************************************************************************************

#Tuples  (Tuples are immutable ,Use tuples when data should stay constant, such as days of the week)
#tuples can also deal with strings or any other data types like lists

numbers = (1,2,3,3,3,3)
print(numbers[0])

#Count (how many times a number appears)
print(numbers.count(3))

#***********************************************************************************************************************
#Dicts   (Stores data in key:value pairs)

student1 = {
    "name":"Meer",
    "age":20,
    "cgpa":3.5
}

#Access
print(student1["name"])
print(student1["age"])
print(student1["cgpa"])

#Change
student1["age"]=21
student1["name"]="Heer"
student1["cgpa"]=3.3
print(student1["name"])
print(student1["age"])
print(student1["cgpa"])

#Add
student1["city"]="Lahore"

print(student1)
#**********************************************************************************************************************

