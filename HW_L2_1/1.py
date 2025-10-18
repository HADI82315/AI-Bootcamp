while (1):
    #if user accidentally entered space in between
    user_input = input("please enter an integer greater than 3: ").replace(' ', '')
 
    if user_input.isdigit():
        if (user_input := int(user_input)) > 3:
            break
        else:
            print("out of range number")
    else:
        print("invalid input")

numbers = range(1,user_input + 1)
if user_input % 2:
    print(*numbers[::2],sep=' ,')
else:
    print(*numbers[1::2],sep=' ,')