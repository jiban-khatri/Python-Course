# Strings = sequence of unicode characters

s = 'Hello'
s1 = "Hello"
s2 = '''Hello'''        # For multiline strings
s2A = """ Jiban """

s3 = str(12)
print(s3)



# === Indexing ===

s = "Jiban"
print(s[0])     

# Positive Indexing =  starts from 0 from start and continues
# Negative Indexing = starts form -1 from last
print(s[-1])



#  == Slicing ==
# extracts more than one part or sub strings from the string

s = "HelloWorld"
print(s[0:4])   # last index is excluded

print(s[0:6:2]) #2 is step size i.e parts to skip

print(s[-1:-5:-1])  

