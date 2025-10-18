while (1):
    #if user accidentally entered space in between
    user_input = input("please enter an integer greater than 3: ").replace(' ', '')
 
    if user_input.isdigit():
        if int(user_input) > 3:
            break
        else:
            print("out of range number")
    else:
        print("invalid input")
print("succesfull")