# Data Types:


## Number Types:
a = 5 
b = 4.00052
complex = complex(4j)
print('type of ' ,type(a))
print('type of ' ,type(b))
print('type of ' ,type(complex))

### User input:
# c = int(input("Enter the Number : "))
c = 45
print('User Input Number : ',c)


## String Types:
str1 = str('string 1 entered')
str2 = 'string 2 entered'
print(f'str 1 value {str1}')
print(f'str 2 value {str2}')

### String functions:

#### multiply the string:
str3 = '_deepanshu'
print(f'string multiply by 3 : {str3*3}')

#### slicing: using slice method
slice1 = slice(-5,-2)
print(f'slice(0,5) : {str3[slice1]}')

#### slicing: using indexing sequence : list[start:end:steps]
print(f'using indexing sequence : {str3[0:8]}')
print(f'using indexing sequence and apply negative index : {str3[-1:]}')


### List, Tuple, set:
#### List : can be changed:  use --- [val1, val2,....]
myList = [1,2,'string_value',2.52,'c',5j]
print('myList storing different datatypes values and it can be modify or changed : ',myList)

#### Operations:
print('length of list : ', len(myList))
print('Access elements : ',myList[-1])

# myList.add(5) 

#### Tuple : can not be changed: use --- ( val1, val2,....)
myTuple = [1,2,'string_value',2.52,'c',5j]
print('myTuple storing different datatypes values and it can not be modify or changed: ',myList)


# ----------- Pending--------------
#### Set : Store unique values: use --- {val1, val2,....}




