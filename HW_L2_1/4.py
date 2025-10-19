
#this class could've been imoported but file name(1.py) prevented us
class OutOfRange(Exception):
    def __init__(self, value, range=(), *args):
        super().__init__( *args)
        self.value = value
        self.range = range

    def __str__(self):
        return f"{self.value} out of {self.range},please try agian."
    
while True:    
    try:
        course_numbers = int(input("please enter number of courses: "))
        if course_numbers < 1:
            raise OutOfRange(value= course_numbers, range=(1,))
    except ValueError:
        print("number of courses shoud be integer")
    except OutOfRange as e:
        print(e)
    else:
        break  