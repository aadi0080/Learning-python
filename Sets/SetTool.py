# num = set()
# print(type(num))
# num.add(2)
# num.add(3)
# num.add(4)
# print(num)

# num.remove(3)
# print(num)
# num.pop()   # return any random value from set and remove it from set
# print(num)        
# num.clear()  # remove all elements from set
# print(num)

# for union or  intersection 
set1 ={12 , 11 , 45 , 34 }
set2 = {23 , 12 , 45 , 0 }
union =set1.union(set2)
print(union)
   
intersection = set1.intersection(set2)
print(intersection)