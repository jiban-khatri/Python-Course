'''
======Everything in Python are Objects.=====

 - - - - mutable and immutable refer to whether an object can be changed after it is created.

 
 ===========Immutable Objects (Cannot Be Changed)========
    If an object is immutable, you cannot modify it after creation.
    If you try to change it, Python creates a new object instead.
        int
        float
        bool
        str
        tuple
        frozenset

        
============Mutable Objects (Can Be Changed)
    If an object is mutable, you can modify it after creation without creating a new object.
    Common Mutable Types:
        list
        dict
        set
        bytearray

'''


'''
======Immutable Example:
x = 5
print(id(x))

x = 8
print(id(x))    # == Memory Address Changes because new object is created
'''



'''
======Mutable Example:
numbers = [1, 2, 3]
print(id(numbers))

numbers.append(4)
print(id(numbers))
'''