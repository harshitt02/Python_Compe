# Write a python function, find_pairs_of_numbers() which accepts a list of positive integers 
# with no repetitions and returns count of pairs of numbers in the list that adds up to n. 
# The function should return 0, if no such pairs are found in the list.
 
def find_pairs_of_numbers(num_list,n):
    count_nums = 0
    for num in num_list:
        for i in num_list:
            sum = num + i
            if sum == n:
                count_nums += 1
    return int(count_nums/2)

num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))









# for num in num_list:
#         for i in num_list:
#             sum = num + i
#             if sum == n:
#                 count += 1
#     return int(count/2)