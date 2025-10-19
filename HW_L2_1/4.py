
#this class could've been imoported but file name(1.py) prevented us
class OutOfRange(Exception):
    def __init__(self, value, range=(), *args):
        super().__init__( *args)
        self.value = value
        self.range = range

    def __str__(self):
        return f"{self.value} out of {self.range}!!"
    
    
while True:    
    try:
        courses_number = int(input("please enter number of courses: "))
        if courses_number < 1:
            raise OutOfRange(value= courses_number, range=(1,))
    except ValueError:
        print("number of courses must be integer!!")
    except OutOfRange as e:
        print(e)
    else:
        break  
    
grades = []
while courses_number:
    try:
        grade = float(input(f"please enter {len(grades) + 1}th grade,must be in (0,20):"))
        if not (0 <= grade <= 20):
            raise OutOfRange(grade,(0,20))
    except ValueError:
        print("grade must be float!!")
    except OutOfRange as e:
        print(e)
    else:
        grades.append(grade)
        courses_number -= 1 
        
av