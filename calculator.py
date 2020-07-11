def get_user_input():
    s = input(">>> ").replace(" ", "") #get user input, removes spaces
    values = [""] #creates list of string values, list is empty right now
    i = 0 #sets variable i to zero
    for c in s: #loop through characters in input 
        if (c.isdigit() and i % 2 == 0) or (not c.isdigit() and i % 2 != 0): #if c is a digit and i is even or c is not a digit then i is odd
            values[i] += c #string at ith position of values gets character c concatenated to it
        else:#otherwise
            i += 1#i = i + 1; i is incremented (increased by one)
            values.append("") # adds empty string to values
            values[i] += c #string at ith position of values gets character c concatenated to it
        
    return values 
    #values has number in the evens positions and operations in the odd positions
    
print("Welcome to Calculator.py")
x = get_user_input()
print(x) ### DEBUG ONLY
ans = ""
if len(x) == 3:
    sign = x[1]

    if (sign == "+"):
        ans = int(x[0]) + int(x[2])
    elif (sign == "-"):
        ans = int(x[0]) - int(x[2])
    elif (sign == "*"):
        ans = int(x[0]) * int(x[2])
    elif (sign == "/"):
        ans = int(x[0]) / int(x[2])

if ans != "":
    print("This is your answer: " + str(ans)) # + means putting two values together for strings
else:
    if len(x) < 3:
        print('Not enough inputs. Please use the format "NUMBER1 OPERATOR NUMBER2".')
    elif len(x) > 3:
        print('Too many inputs. Please only include 2 numbers seperated by an operator.')
    else:
        print(f'I do not recognize the operator "{sign}".')