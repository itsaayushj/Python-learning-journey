# dictionary = a collection of {key : value} pairs
#               ordered and changeable. No dupes

count ={
  "A" : 1 , 
  "B" : 2 , 
  "C" : 3 , 
  "D" : 4
}
# print(count)
# key = count.keys()
# print(key)
# value = count.values()
# print(f"{value} is the value")
 
# items = count.items()
# print(items)
# for key , value in items :
#     print(key , value )
print(count.get("B"))
count.update({"E": 5})
