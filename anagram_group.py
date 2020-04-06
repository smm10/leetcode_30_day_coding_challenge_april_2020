

strs = ["eat","tea","tan","ate","nat","bat"]


anagram_group = []
        
        #sorted_temp = ""
        
updated_length = len(strs)
"""
for i in range(0,updated_length):
    new_arr = []
    new_arr.append(strs[i])
    for j in range(i+1,updated_length):
        print(i)
        print(j)
        print(updated_length)
        print(strs)
        print(strs[j])
        print("###############")
        if(''.join(sorted(strs[i])) == ''.join(sorted(strs[j]))):
            new_arr.append(strs[j])
            strs.pop(j)
            
            updated_length = len(strs)

"""

i = 0
j = 0 

while(i<updated_length):
    new_arr = []
    new_arr.append(strs[i])
    j = i+1
    while(j<updated_length):
        if(''.join(sorted(strs[i])) == ''.join(sorted(strs[j]))):
            new_arr.append(strs[j])
            strs.pop(j)
            
            updated_length = len(strs)

        j = j+1
        
    anagram_group.append(new_arr)
    new_arr = []
    i = i+1
            
    
    

   
    
    
print(anagram_group)