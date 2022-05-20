'''
funct+oops:-
50 :- 35+
linear dsa:- 
non linear :- trees (b tree, b+, red black)
DP:- 4 lecs 8hrs

lambda,map,filter,decorators,closures,iterators,genrators

'''

'''
Create a Book class that has two attributes:

.title
.author
and two methods:

A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:

Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"


Create a class named User and create a way to check the number of users (number of instances(bojects)) that were created, 
so that the value can be accessed as a class attribute.

instance var/attri local :- self.one  self.name
class var/attri    global:- 


Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"
'''

class User:
    count_numb = 0  #class var/atttri

    def __init__(self, name): 
        self.name = name;   #instance var/atrri
        User.count_numb+=1; 
        self.my_count = User.count_numb
    

# u1 = User("A"); 

# u2 = User("B"); 
# u3 = User("C"); 
# print(u2.user_count())


class demo:
    def __init__(self,f_name):
        self.f_name = f_name
        print("Good Morning...!")

    def show(self):
        print("Good Morning", self.f_name)
    
obj1 = demo("harry")  


class Book:
    def __init__(self,title,author):
        self.title= title, 
        self.author = author

    def get_title(self):
        return f"Title: {self.title}"

    def get_author(self):
        return self.author

# PP, H, WP = Book(), Book(), Book()
# PP.title, H.title, WP.title = "Jane Austen", "Hamlet", "War and Peace"
# PP.author, H.author, WP.author = "J.K Rowling", "William Shakespeare", "Leo Tolstoy"


'''

A country can be said as being big if it is:
name of the country
Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:


Population is greater than 250 million. 250*10**6
Area is larger than 3 million square km. 3*10**6


Also, create a method which compares a country's population density to another country object.
 Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}

Examples
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Aus
aus.compare_pd(andora) ➞ "Andorra has a larger population density than Aus

'''

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 250*10**6 or self.area > 3*10**6
        
 
    def compare_pd(self, other_country):
        
        if self.population/self.area > other_country.population/other_country.area:
            print(f"{self.name} has larger population density than {other_country.name} ")
        elif self.population/self.area < other_country.population/other_country.area:
            print(f"{self.name} has smaller population density than {other_country.name} ")
        # density1 = self.population/self.area
        # density2 = other_country.population / other_country.area

        # if(density1 > density2):
        #     print('{} has larger population density than {}'.format(self.name, other_country.name))
        # else:
        #     print('{} has smaller population density than {}'.format(self.name, other_country.name))

# australia = Country('australia', 23545500, 7692024)
# andorra = Country('andorra', 76098, 468)

# print(australia.is_big)
# print(andorra.is_big)

# andorra.compare_pd(australia)
# australia.compare_pd(andorra)

'''
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
Examples
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"


Write a program that returns a list of all the numbers from 1 to an integer argument. 
But for multiples of three use “Fizz” instead of the number and for the multiples of five use “Buzz”. For numbers which are multiples of both three and five use “FizzBuzz”.

Example
fizz_buzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]

fizz_buzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
Notes
Make sure to return a list.

'''
def multiples(input):
    list1= []
    for i in range(1,input + 1):
        if i%3==0:
            if i%5==0:
                list1.append('FizzBuzz')
            else:
                list1.append('Fizz')
        elif(i%5==0):
           list1.append('Buzz')
        else:
            list1.append(i)
    
    return list1

input = (input('Enter integer: '))
print(multiples(int(input)))
print(list1)



'''

Given a list of even length, copy the half with the higher sum of numbers to the other half of the list. 
If the sum of the first half equals the sum of the second half, return the original list.

Examples
balanced([1, 2, 4, 6, 3, 1]) ➞ [6, 3, 1, 6, 3, 1]
# 1 + 2 + 4 < 6 + 3 + 1  sol = [6, 3, 1, 6, 3, 1]

balanced([88, 3, 27, 5, 9, 0, 13, 10]) ➞ [88, 3, 27, 5, 88, 3, 27, 5]
# 88 + 3 + 27 + 5 > 9 + 0 + 13 + 10  sol = [88, 3, 27, 5, 88, 3, 27, 5]

balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]) ➞ [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
# 7 + 5 + 2 + 6 + 1 + 0 = 1 + 5 + 2 + 7 + 0 + 6  sol =  [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
Notes
The length of the list is even.

'''

def checker_maker(my_list):
    length = len(my_list)
    half1 = my_list[:length//2]
    half2 = my_list[length//2:]
    sum1 = sum(half1)
    sum2 = sum(half2)
    if sum1>sum2: return half1 + half1
    if sum1<sum2: return half2 + half2
    else: return my_list
print(checker_maker([0,5,5,6,3,1]))

'''
Write a function that takes a list and determines whether it's strictly increasing,
 strictly decreasing, or neither.

Examples
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater 
than the 0-indexed 1.


10 test case

'''



def check(numList):
    if sorted(set(numList)) == numList:
        return "increasing"
    if sorted(set(numList),reverse=True) == numList:
        return "decreasing"
    return "neither"
print(check([1,2,1]))


'''
test 3
fun
oops
dsa


Trees non linear dsa

dp

stack queue   linear
trees         non linear
Graphs        implementation
DP  + letcode or both

31st may oops
linear non linear

dsa:- dbms trees graphs 


dp +letcode


trees

b trees 
b+ trees

5 non linear 

keys = 1,57,9,3,4,10,15,19
order = m = 5
b+ tree


funct test :- 

last day:- all test link


'''
