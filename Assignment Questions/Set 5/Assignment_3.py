# Assignment Set 3 - Question 3

def check_double(num):
    double = 2 * num
    dou = str(double)
    n = str(num)
    count = 0
    if len(dou) == len(n):
        for i in dou:
            if i in n:
                count += 1
        if count == len(n):
            return True
        else: 
            return False
    else:
        return False

a = int(input("Enter a number"))
print(check_double(a))