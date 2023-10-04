# Task
# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()
    print(True in list(map(lambda n:n.isalnum(),s)))
    print(True in list(map(lambda n:n.isalpha(),s)))
    print(True in list(map(lambda n:n.isdigit(),s)))
    print(True in list(map(lambda n:n.islower(),s)))
    print(True in list(map(lambda n:n.isupper(),s)))
