
arr = [2,2,1,1,7]


# The below approach can only be used if the no.s present is less that the index. If the numbers present
# is more than the index it will result in an List index out of bounds runtime error

'''
for i in range(len(arr)):
        arr[abs(arr[i])] =  arr[abs(arr[i])] * (-1)
        #print(i)
        #print(arr)
        #print("##################")

#print(arr)


for i in range(len(arr)):
    if arr[i]<0:
        #print(i)

'''


arr[0] = arr[0] ^ arr[1] 
#other best and easy approach
for i in range(2,len(arr)):
    
        arr[0] = arr[0] ^ arr[i]
print(arr[0])

