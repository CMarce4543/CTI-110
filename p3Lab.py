#Christian Marcellino
#3/17/24
#P3Lab

#This program will take information and determine if there is a leap year.

is_leap_year = False
 
# User needs to input the year.

year = int(input('Please Enter a year:' ))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

    is_leap_year = True

#if/else response. 

if is_leap_year:

    print(f"{year} - leap year")

else:

    print(f"{year} - not a leap year")
