fruits = ["Apple","Orange","Banana"]
print(fruits[2])

for x in fruits:
    print(x)



if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")

print(len(fruits))

fruits.append("Grape")
fruits.insert(1,"Papaya")
fruits.remove("Orange")
print(fruits)

y= fruits.pop()
print(y)
print(fruits)
print("clrear fruit")

#fruits.clear()
#print(fruits)

#del fruits
#print(fruits)

newfruits = list(("Apple","Orange","Banana"))
print(newfruits)
fruits.extend(newfruits)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)