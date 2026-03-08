# Nested Loop =  Loop inside Loop

# print pairs of 1-3

for i in range(1,4):
    for j in range(1,4):
        print(i,j)


rows = int(input("Enter no. of rows: "))
# for i in range(1,rows+1):
#     print('*'*i)

for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end="")
    print('')                            





# 
rows = int(input("Enter no. of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end="")     
    for k in range(i-1,0,-1):
        print(k,end="")                      
    print()



# 

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start,end+1):
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
     print(i)
                   