#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func == None:
        return sum(list_of_num)
    else:
        for i in list_of_num:
            return sum(filter_func(list_of_num))
    

def even(data):
    new_list = []
    for i in data:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

def odd(data):
    new_list = []
    for i in data:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

sample_data = range(1,11)



print(sum_of_numbers(sample_data,None))