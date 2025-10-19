class OutOfRange(Exception):
    def __init__(self, value, *args):
        super().__init__( *args)
        self.value = value

    def __str__(self):
        return f"{self.value} is less than 3 and is invalid,please try agian"

while (1):
    try:
        user_input = int(input("please enter an integer greater than 3: "))
        if user_input < 3:
            raise OutOfRange(user_input)
    except ValueError:
        print("input must be integer only,please try again")
    except OutOfRange as e:
        print(e)
    else:
        break
        

numbers = range(1,user_input + 1)
if user_input % 2:
    print(*numbers[::2],sep=' ,')
else:
    print(*numbers[1::2],sep=' ,')