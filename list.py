# hg----single line comment
""" shivANI
shkdnkfkfkfkfkkfvf
djfjfhjfhjfj-----multiline comment"""


# Balance = 10
# balance = 8
# print(Balance)
# print(balance)

# q1 = 10
# print('q1')
# q3 = 9
# print('q2')
# print(q3)

# float
# y = 89.0
# print(y)
# print(type(y))

# list (multiple elements at one memory)

l1=[10,20,30,40,50,60,70,80,90,100,10]

# print(l1.count(70))
l1.sort()
print(l1)

l1.insert(0,100)
print(l1)

l1.pop(5)   #remove given index value,remove last index
print(l1)


# program 2
#      0        1        2        3        4     5
l=["shivani","Pranay",'Aditya','Aditya','Anuj','Abhay']
l.append('Samrat')
print(l)

l.extend(['mahi','kanha'])
print(l)

l.insert(2,'Aayush')
print(l)

l1=l.count('Aditya')
print(l1)
# ------------------------------------------
lst=[20,40,30,10,60,50,70,80,100,90]

lst.sort()
print(lst)

# lst.pop() #remove last element
# print(lst)

# lst.clear()
# print(lst)

for i in lst:
    print(i)

above50=[]
for i in lst:
    if i >= 50:
        above50.append(i)
print(above50)

for i in range(len(lst)):
    print(f'{i} :- {lst[i]}')
# -------------------------------------
first_Name='shivani'
last_Name='Hedau'

print(f'My first name is {first_Name} and last name is {last_Name}')
print("my first name is",first_Name,"and last name is",last_Name)

