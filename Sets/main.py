'''
-- Collection of unordered items
-- they must be unique, doesn't contain duplicate 

NOTE: -- Sets are mutable but set elements are immutable

'''

nums = {1,2,3,4}
print(nums)
print(type(nums))
# print(nums[2])    NOT POSSIBLE



# ==== Creating Empty Set ====

# set2 = {}   # This is a dictionary not set
# print(type(set2))

# -- Correct method ---
new_set = set()
print(type(new_set))

# ---Set Methods----
collection = set()
collection.add(1)
collection.add(6)
collection.add(2)
collection.add(1)
print(collection)

collection.remove(2)
print(collection)

collection.pop()    #removes random value
print(collection)



# ========== Set Union and Set Intersection

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

intersect_set = set1.intersection(set2)
union_set = set1.union(set2)

print(intersect_set)
print(union_set)


