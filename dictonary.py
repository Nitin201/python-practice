data = {"name": "python", "pages": 250, "author": "nitin", "price": 200}
data["price"]=500
print(len(data))
#data.get("name")
copy = data.copy()
print(copy)

#using for loop

for x in data.keys():
    print(x)

for x in data.values():
    print(x)


for x,y in data.items():
    print(x,y)



