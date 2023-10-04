# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        command = input().split()
        if command[0] == "append":
            list.append(int(command[1]))
        elif command[0] == "insert":
            list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(list)
        elif command[0] == "pop":
            list.pop()
        elif command[0] == "sort":
            list.sort()
        elif command[0] == "remove":
            list.remove(int(command[1]))
        else:
            list.reverse()
        
