#Basic Print all integers from 0 to 150
for basic in range(1,151):
    print(basic)

#Multiples of 5 from 5 to 1000
for five in range(5,1005,5):
    print(five)

#Counting, the Dojo Way
def count_dojoway():
    for count_dojoway in range (0,101):
        if count_dojoway % 5 == 0:
            print("Coding")
        if count_dojoway % 10 == 0:
            print("Coding Dojo")
        else:
            print(count_dojoway)
count_dojoway()

#Whoa. That Sucker's Huge
oddtotal = 0
for huge in range(1,500001,2):
        oddtotal += huge
print(oddtotal)

#Countdown by Fours
for four in range(2018,0,-4):
    print(four)

#Flexible Counter
def flex_countdown(low, high, mult):
    for flex in range(low, high + 1):
        if flex % mult == 0:
            print(flex)

flex_countdown(2,9,3)