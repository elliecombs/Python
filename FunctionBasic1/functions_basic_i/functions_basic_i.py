#1#Prediction output is 5 food groups
def number_of_food_groups():
    return 5
print(number_of_food_groups())


# 2 None + 5 the number of days in a week are undefined aka output is undefined
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())



#3 Output: 5 there can only be one return
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 Output: 5 nothing after return
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 Output: 5 then none because nothing is returned after x
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 output: none because no return means none
def add(b,c):
    print(b+c)
    # return b+c
print(add(1,2) + add(2,3))


#7  Output 25 because concatenate operation is joining 2 strings together
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 Print 100, 10 because 100 is defined as b and 100 will be greater than 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 Output: 7, 14, 21 because 2 is less than 3 return is 7 and 5 is greater than 3 return is 14 and 7 + 14 is 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 output: 8 because 3+5 is 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 Output: 500, 500, 300, 500 because there is no return after line 83 
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 Output: 500, 500, 300, 500 because the return was not in the code block
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 Output: 500, 500, 300, 300 because the new value of b is 300 when line 110 is called go up to foobar function then print the new value of b.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 Output 1, 3, 2 follow what function is being called in this case foo, then bar, then foo
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 output: 1, 3, 5, 10 because y is assigned to the value of the foo function
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)