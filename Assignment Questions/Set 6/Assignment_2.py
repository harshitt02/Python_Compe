def find_duplicates(list_of_numbers):
    new_lst = []
    for i in range(0, len(list_of_numbers)):
        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[j] == list_of_numbers[i]:
                new_lst.append(list_of_numbers[i])
    
    return list(set(new_lst))

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)