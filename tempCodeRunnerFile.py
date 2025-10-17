data = {10,100,200,10}
data.add(500)
#data.remove(100)
#data.clear()
#del data

print(len(data))

#for x in data:
 #   print(data)

#set methods

#union
a ={10,20,30}
b = {10,100,200,40,20,30}

u = a.union(b)
print(u)
i = a.intersection(b)

print(i)

#subset
print(a.issubset(b))
print(b.issubset(a))

#superset
print(a.issuperset(b))
print(b.issuperset(a))