# reversing a number
num = int(input("Enter a number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(f"The given number is {temp} and reverse is {reverse}")

# ---------------------------------------------------------------

# GCD of a number
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(gcd(8, 12))  # Outputs: 4

# ---------------------------------------------------------------

#LCM of a number
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# Example usage:
print(lcm(12, 15))

# ---------------------------------------------------------------

#Calculating factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage:
print(factorial(5))  # Outputs: 120

# ---------------------------------------------------------------

# Combinations
def combination(n,r):
    return factorial(n)/(factorial(r) * factorial (n-r))

# Example usage:
print(combination(5,2))

# ---------------------------------------------------------------

# function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")

# ---------------------------------------------------------------

# Fibonacci Series

num = int(input("Enter the number:"))
n1, n2 = 0, 1
print("Fibonacci series: ", n1, n2, end =" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end = " ")

print()

# ---------------------------------------------------------------

#Perfect number

n = int(input("Enter any number: "))
sump= 0
for i in range(1, n):
    if(n % i == 0):
        sump= sump + i

if (sump == n):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

# ---------------------------------------------------------------

# To find Leap year

year = int(input("Enter Year:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a Leap year")


# ---------------------------------------------------------------

# reversing a string

str1 = "Analytics Vidhya" 
str2 = "" 
for i in str1: 
    str2 = i + str2

print("The original string is: ",str1) 
print("The reversed string is: ",str2)

# ---------------------------------------------------------------

# Finding missing elements in List

test_list = [3, 5, 6, 8, 10]
 
# using list comprehension
# Finding missing elements in List
res = [ele for ele in range(max(test_list)+1) if ele not in test_list]

print('The list of missing elements : ' + str(res))


# ---------------------------------------------------------------

# Concatenate two lists

lst1= ['W', 'a', 'w','b']
lst2 = ['e', ' ','riting','log'] 
lst3 = [x + y for x, y in zip(lst1, lst2)] 
print(lst3)


# ---------------------------------------------------------------

# square of every element in a list
lst = [1, 2, 3, 4]

result = [x**2 for x in lst]
print(result)

# ---------------------------------------------------------------

# Checking for Prime number

num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Another method using sqrt

from math import sqrt
def prime_or_not(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return "Not a prime number"
        return "Prime number"

# ---------------------------------------------------------------

# Calculating factorial using recursion

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
factorial(5)

# ---------------------------------------------------------------

# How do you find the minimum value in a list with a lambda function?

from functools import reduce

b = [3, 1, 4, 1, 5, 9, 2, 6]
minimum_value = reduce(lambda x, y: x if x < y else y, b)
print(minimum_value)  # Outputs: 1


# Write a code to get the minimum value in a dictionary.
dict_ = {
    'a': 10,
    'b': 5,
    'c': 15,
    'd': 2
}

min_value = min(dict_.values()) # Outputs 2

# If you want the key associated with the min value:

key_with_min_value = dict_[min(dict_.keys(), key=(lambda k: dict_[k]))]
print(key_with_min_value)  # Outputs: 'd'
