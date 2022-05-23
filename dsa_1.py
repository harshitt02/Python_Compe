#lex_auth_0127426166978887681375

def merge_list(list1, list2):
    merged_data=""
    # j = -1
    for i in range(len(list1)):
        data1 = ""
        data2 = ""
        # j -= -1 
        j = len(list2)-i-1
        if list1[i]:
            data1 = list1[i]
        if list2[j]:
            data2 = list2[j]
        merged_data += data1 + data2 +" "
        
          
    
    #write your logic here
    return merged_data.strip()

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)