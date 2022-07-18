# n = input('enter the value: ')
# n = int(n)
# for i in range(n) :
#     op = input('enter operation: ')
#     op_list = op.split()
#     print(op_list)
#     if op_list[0] == 'add':
#         first_number = int(op_list[1])
#         second_number = int(op_list[2])
#         print(first_number + second_number)
#     elif op_list[0] == 'sub':
#         first_number = int(op_list[1])
#         second_number = int(op_list[2])
#         print(first_number - second_number)
#     elif op_list[0] == 'multi':
#         first_number = int(op_list[1])
#         second_number = int(op_list[2])
#         print(first_number * second_number)
#     elif op_list[0] == 'divide':
#         first_number = int(op_list[1])
#         second_number = int(op_list[2])
#         print(first_number / second_number)
#     elif op_list[0] == 'module':
#         first_number = int(op_list[1])
#         second_number = int(op_list[2])
#         print(first_number % second_number)
    
# take input from user in number and add those no. the range of the no. is 2-9
# n = input('enter the no. = ')
# n = int(n)
# for i in range(n):
#     op = input('enter operation: ')
#     op_list = op.split()
#     total  = 0
#     total_mult = 1
#     print(op_list)
#     if op_list[0] == 'add':
#         for j in op_list[1:]:
#             total = total + int(j)
#         print(total)
#     if op_list[0] == 'multi':
#         for j in op_list[1:]:
#             total_mult = total_mult * int(j)
#         print(total_mult)

# Factorial of number 

# n = input('enter the no.: ')
# n = int(n)
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print("the factorial of",n ,"is",fact)

#palindrome

# string = input("enter the string: ")
# if string == string[::-1]:
#     print("palandrome")
# else:
#     print("not a palandrome")

# take n input of ascii then convert them into a string

value = int(input("enter the value: "))
s = ''
for i in range(value):
    ascii_number = int(input())
    char = chr(ascii_number)
    s += char
    print(s)

# p = input()
# p_list = p .split()
# print(p_list)
# s = ''
# for i in p_list:
#     s += chr(int(i))
#     print(s)    
n = input()
if len(n)  != 16:
    print('Input is not of 16 digit')

for i in n:
    if ord(i) >= 65 and ord(i) <= 97:
        print('capital letter found')
    elif ord(i) >= 110 and ord(i) <= 136:
        print('small letter also found')
    elif some_condition:
        some_statemetn
    elif some_condition:
        some_statement
    else:
