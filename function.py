# def greet():
#     print("Hello, World!")

# greet()

#

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact

# fact_of_5 = factorial(5)
# fact_of_10 = factorial(10)

# print(fact_of_5)
# print(fact_of_10)

# n = int(input('enter the no.: '))
# def table(n):
#     for i in range(1,11):
#         print(i*n)
    
# table_of_n = table(n)

# lst = ['1','2','4']
# def list():
#     print(lst)

# list()
 
# def return_list():
#     return[1,2,3,4]


# def bool():
#     p = input('enter a string: ')
#     for i in p:
#         if i == p.upper():
#             return[True]
#         else:
#             return[False]
# ans = bool()
# print(ans)

# def is_string_upper(string):
#     return string.isupper()

# asc = input('enter string: ')

# def value_asc(x):
#     total = 0
#     for i in range(0,len(x)):
#         ad = ord(asc[i])
#         total = total + ad
#     x = print(total)
#     return(x)
# value_asc(asc)


# def sum_of_ascii(input_string):
#     sum_ = 0
#     for i in input_string:
#         sum_ += ord(i)
#     retun(sum_)
# print(sum_of_ascii)

# write an fuction to return take 2 string 

# username = input('enter the name:')
# password = input('enter password:')
# def generate(username,password):   
#     final = username[:4] + password[-4:]
#     print(final)
# generate(username,password)


# char = input('enter character: ')
# def character_index():
#     total = 0
#     for i in range(len(char)-1):
#         if (ord(char[i])+1) == ord(char[i+1]):
#             total += 1
#     print(total)
# character_index()

lst = ['1','2','3','4','5','6','7']
def even_lst(lst):
    for i in lst:
        if (int(i)%2 == 0):
            print("Even")
        else:
            print("Odd")

even_lst(lst)
