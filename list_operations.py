my_list = []

n = int(input())

for _ in range(n):
    command = input().split()
    
    try:
        if command[0] == "insert":
            i, e = map(int, command[1:])
            if i < 0:
                print(f"Error: Invalid index {i} for insert")
                continue
            my_list.insert(i, e)
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            e = int(command[1])
            if e in my_list:
                my_list.remove(e)
            else:
                print(f"Error: Element {e} not found in list")
        elif command[0] == "append":
            e = int(command[1])
            my_list.append(e)
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            if my_list:
                my_list.pop()
            else:
                print("Error: Cannot pop from an empty list")
        elif command[0] == "reverse":
            my_list.reverse()
        else:
            print(f"Error: Unknown command {command[0]}")
    except ValueError as ve:
        print(f"Error: Invalid input for command {command} - {str(ve)}")
    except IndexError as ie:
        print(f"Error: Index out of range for command {command} - {str(ie)}")