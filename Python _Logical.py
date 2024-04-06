li=[40,10,10,30,50,40]
duplicate=[]

for i in li:
    if li.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)
# ----------------------------------------
# Find the maximum element in a list:


li2=[10,20,30,40,50,60,70,80,90,100]
max_val=li2[0]

for i in li2:
    if i  > max_val: #10>10
        max_val = i

print(max_val)

li3=["shivani","divya","neha","aditi","shivani"]
newli=[]
for i in li3:
    print(i)
    if i not in newli:
        newli.append(i)

print(newli)

# ----------------------------------------------------

# 8pm=js
# 8am=cypress
# 9am = python

# --------------------------------------------

dic ={
    "FirstName":"shivani",
    "lastname":"hedau",
    "rollno": 123
}

for k,v in dic.items():
    print(f'{k}:{v}')