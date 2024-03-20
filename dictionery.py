
info = {
    "first_name":"shivani",
    "last_name":"hedau",
    "age":10,
    "rollNo":45
}

info2 = info
info2['age'] = 89

# print(info)
# print(info2)

info3=info.copy()

info3['age']=28
print(info3)
print(info)

# ---------------------------------------------------------------------
dic={
    'firstName':'Shivani',
    'lastName':'Hedau',
    'age':28,
    'rollNo':270494
}

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

for k,v in dic.items():
    print(f'{k} : {v}')


# print(dic.get('firstName'))
#
# dic.pop('rollNo')
# print(dic)
#
# dic.popitem()
# print(dic)

dic.update({'city':'Nagpur'})
print(dic)

dic['Nationality']='Indian'
print(dic)
# --------------------------------------
e = dict.fromkeys(["firstName","LastName","Age"])
print(e)
# -----------------------------------------

# info3 = {
#     "admin":"shivani",
#     "customer":"pranay",
#     "support":"Romi"
# }
#
# info3.setdefault("manager")
# print(info3)

# -------------------------------------------------------

