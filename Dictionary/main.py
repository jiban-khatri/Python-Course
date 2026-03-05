'''
--- Used to store values in 'key':'value' pairs
--- Are unordered, mutable(changable) and don't allow duplicate keys
'''

details = {
    "name" : "Ram",
    "age" : 18,
    "address" : {
        "per_address" : "Dang",
        "temp_address" : "Kathmandu"
    }
}
print(details)
print(type(details))
print(details["name"])
print(details["address"]["per_address"])

details["name"] = "Jiban" #change value
print(details["name"])

# Add new key value
details["country"] = "Nepal"
print(details)


print(details.keys())       # Get keys of dictionary
print(len(details))

print(details.values())     #returns values 
print(details.items())      # Returns all (key,vals) pairs in tuples

print(details.get("name"))  #returns value acc to key


print(details["surname"])   # -> Error
print(details.get("surname"))  # --> Returns 'None'


details.update({'city' : 'kTM'})
print(details)


# ===========================================================
'''
dict2 = details
print(dict2)

dict2["age"] = 20
print(dict2)
print(details)

Note:
============= Changing or updating one dictionary also affect or changes another dictionary 
This is called Swallow Copy
==========

'''

# =======================================================

"""

dict = details.copy()
print(dict)

dict["age"] = 20
print(dict)
print(details)

===== This is called Deep Copy. Here changing one doesn't affect other. All are completely independent ===

"""


name = input("Enter your name: ")
mark1 = int(input("Enter mark in first subject: "))
mark2 = int(input("Enter mark in second subject: "))
mark3 = int(input("Enter mark in third subject: "))

student_report = {}

student_report.update({"name": name,"marks" : {"sub1" : mark1, "sub2" : mark2, "sub3" : mark3 } })

print(student_report)

