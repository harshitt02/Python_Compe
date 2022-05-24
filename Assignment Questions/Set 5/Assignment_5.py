# Assignment Set 5 - Question 5

'''
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

    The number and its double should have exactly the same number of digits.

    Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.

'''
marks_list=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count = 0
    avg = sum(marks_list)/len(marks_list)

    for i in marks_list:
        if i > avg:
            count += 1
    percentage = (count / len(marks_list)) * 100
    return percentage

def generate_frequency():
    freq_list = []
    stu_count = 0
    for i in range(0, 26):
        for j in marks_list:
            if j == i:
                stu_count += 1
        freq_list.append(stu_count)
        stu_count = 0
                
    
    return freq_list
            

def sort_marks():
    sorted_list = sorted(marks_list)
    return sorted_list

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())