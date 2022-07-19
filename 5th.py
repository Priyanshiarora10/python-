# psd = input("Enter a password ")
# for i in range(3):
#     p = int(0)
#     q = int(0)
#     r = int(0)
#     s = int(0)
        
#     if len(psd) > 0 and len(psd) <= 5:
            
#         for j in range(0,len(psd)):
                
#             if ord(psd[j]) >= 48 and ord(psd[j]) <= 57:
#                 p = int(1)  # numbers
#             if ord(psd[j]) >= 65 and ord(psd[j]) <= 90:
#                 q = int(1)  # Capital Alphabets
#             if ord(psd[j]) >= 97 and ord(psd[j]) <= 122:
#                 r = int(1)  # small alphabets
#             if ord(psd[j]) >= 33 and ord(psd[j]) <= 47 or ord(psd[j])  == 64 :
#                 s = int(1)   # special symbols
#     print(p,q,r,s)
#     if p == 1 and q == 1 and r == 1 and s == 1:
#         print('valid password')
#         break
#     else:
#         continue

# n = input()
# map_ ={}

# for i in n:
#     if i in map_:
#         map_[i] += 1
#     else:
#         map_[i] = 1
# print(map_)

# dict = {}
# p = input('enter a name: ')
# s = p.lower()

# for i in s:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)


# lst = []
# while True :
#     command = input()
#     command = command.split()
#     if command[0] == 'stop':
#         break
#     elif command[0] == 'push':
#         lst.append(command[1])
#     elif command[0] == 'pop':
#         p = lst.index(command[1])
#         lst.pop(p)
#     else:
#             print('invalid')

#     print(lst)


map_ = {}
while True:
    stud_info = input()
    """
    stop
    maths shivank
    maths aman
    english aman
    """
    stud_info = stud_info.split()
    """
    ["stop"]
    ["maths", "shivank"]
    ["maths", "aman"]
    """
    if stud_info[0] == 'stop':
        break
    else:
        if stud_info[0] in map_:
            map_[stud_info[0]].add(stud_info[1])
        else:
            map_[stud_info[0]] = {stud_info[1]}
            # map_[stud_info[0]].add(stud_info[1])

print(map_)       