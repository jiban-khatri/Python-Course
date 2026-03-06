# -- Arithmetic Operator -- 
print(5+6)  #11
print(5-6) #-1
print(5*6)  #30
print(5/6)  #0.8333
print(5%2)  #1 -- returns remainder
print(5**2) #25 -- ** = power


# == Relational Operator ==
print(2 == 2)   # equals to
print(4>5)  #greater than
print(4<5)  #less than  
print(4>=4) #greater than equal
print(4<=3) #less than equal
print(4 != 2)   # Not 




#  === Logical Operator ===

print(1>3 and 3>2)  #both must be true
print(1>3 or 3>2)  #at least one must be true
print(not (2 ==2 ))  #reverses



#  ==  BitWise Operator ==

a = 2      # binary: 10
b = 3      # binary: 11

result = a & b  #AND
print(result)   # 2

result = a | b  #OR
print(result)   # 3

result = a^b    #XOR
print(result)


# -- Note : 'And' and '&' both are different


#  === Assignment Operators ===

a = 2
print(a)

a+=2    # a = a+2
print(a)
# ....... more.



# ==== Membership Operators
nums = [1,2,3,4,5]
print(2 in nums)    # True
print(5 not in nums) #False



#  == Identity Operator ==
a = [1,2]
b = a
print(a is b)   #true
print(a is not b)   #False

c = [1,2]
print(c is a)   # False



# == Program to get sum of a 3 digit number entered by user

number = int(input("Enter a number: "))    #345
a = number%10       #5
number //= 10       # 34
b = number%10       # 4
number //= 10       # 4
c = number%10       # 4
print(a+b+c)    # 5+4+4
