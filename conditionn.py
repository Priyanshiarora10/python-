#fname = 'Piyu'
#lname = 'Arora'

#if fname == 'Piyu' or lname == 'Arora':
 #   print('yes first name is Piyu')
#else:
 #   print('no first name is not Piyu')


# if 'Shivank' in ['a','b','c'] :
#     print ('p' in 'Shivank')
# elif 'k' in 'Aakash' :
#     print('Akash has k in spelling')
# else :
#     print('kuch ni mila')

# name = input('enter the string :')
# for i in name :
#     if (ord(i)%2==0):
#         print("i is even for " +i)

#take 5 input from user and append all input in list

# n = int(input('enter the value : '))
# print(n)
# lst = [ ]
# for i in range(n) :
#     var = input ()
#     lst.append(var)
# print(lst)

# take n input from user 

n = int(input('enter the value: '))
map_ = {
    'str' : [],
    'int' : [],
    'float' : []
} 
for i in range(n):
    dt = input('enter datatype: ')
    value = input('enter value of above datatype: ')
    if dt == 'str':
        map_['str'].append(value)  
    elif dt == 'int':
        map_['int'].append(value)
    elif dt == 'float':
        map_['float'].append(value)
    else:
        print('please initialize a empty for {dt}'.format(dt))
print(map_)

a = 6
b = 5
