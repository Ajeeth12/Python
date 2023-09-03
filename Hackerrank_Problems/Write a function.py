# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    
    # Write your logic here
    # divided by 100 means century year
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        
        # change leap to True
        leap = True
 
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
         
        #Change leap to true
        leap = True
 
    #else not a leap year
    else:      
        pass
            
    return leap

year = int(input())
