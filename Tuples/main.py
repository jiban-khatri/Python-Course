#   Tuples are same as list but are ' IMMUTABLE '
#   we use () to create tuples

nums = (4,1,9,17,12,1)

# print(nums)
# print(type(nums))

# print(nums[3])

# nums[2] = 18    # NOT POSSIBLE

# ==== If we create tuple only with one element then we must add ' , ' at last or else python will treat  it as Integer

tup = (1,)
print(type(tup)) 


print(nums.index(9))
print(nums.count(1))