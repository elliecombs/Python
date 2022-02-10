# 1 Countdown
for x in range (5,0,-1):
    print(x)

#2 Print and return
b = 1
print(b)
def print_and_return():
    b = 2
    return(b)
b = print_and_return()
print(b)

#3 First Plus Length
def first_plus_length(some_list):
    return (some_list[0] + len(some_list))
print (first_plus_length([1,2,3,4,5]))

#Value Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    else: 
        newlist = []
        #this is a new list for new values
        for i in range(0,len(list)):        #list[i] = list[0]: 5, list[i] = list[1]: 2; list[i] = list[2]: 3; list[i] = list[3]:2
            # print(list[i])
            if list[i] >list[1]:
                # print(list[i])
                newlist.append(list[i])
        #how many values are in this list?
        #return the new list
        print(len(newlist))
        return newlist
        
print(values_greater_than_second([5,2,3,2,1,7]))
print("************")
print(values_greater_than_second([1]))
print("************")
print(values_greater_than_second([4,5,6,7,8,9,89,100]))

#This length, That Value
def functionhappy(size,value):
# def function_name(size, value):
    newlist =[]
    # need an empty list to add things to
    for i in range(size):
        newlist.append(value)
    # loop: for size of number
        # add value
    return newlist
    # return list
print(functionhappy(4,7))
print(functionhappy(6,2))





def length_and_value(4,7):
    print(length_and_value(size, value))