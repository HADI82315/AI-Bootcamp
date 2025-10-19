class OutOfRange(Exception):
    def __init__(self, value, range=(), *args):
        super().__init__( *args)
        self.value = value
        self.range = range

    def __str__(self):
        return f"{self.value} out of {self.range}!!."

while (1):
    try:
        user_input = int(input("please enter an integer greater than 3: "))
        if user_input < 3:
            raise OutOfRange(user_input,range=(3,))
    except ValueError:
        print("input must be integer only!!")
    except OutOfRange as e:
        print(e)
    else:
        break
        

numbers = range(1,user_input + 1)
if user_input % 2:
    print(*numbers[::2],sep=' ,')
else:
    print(*numbers[1::2],sep=' ,')