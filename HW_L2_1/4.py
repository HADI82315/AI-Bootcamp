import time

#this class could've been imoported but file name(1.py) prevented us
class OutOfRange(Exception):
    def __init__(self, value, range=(), *args):
        super().__init__( *args)
        self.value = value
        self.range = range

    def __str__(self):
        return f"{self.value} out of {self.range}!!"
    
def grade(score):
    grade: str
    if score >= 18:
        grade = "A"
    elif score >= 15:
        grade = "B"
    elif score >= 12:
        grade = "C"
    else:
        grade = "F"
        
    return grade
       
while True:    
    try:
        courses_number = int(input("please enter number of courses: "))
        if courses_number < 1:
            raise OutOfRange(value= courses_number, range=(1,))
    except ValueError:
        print("number of courses must be integer!!")
    except OutOfRange as e:
        print(e)
        time.sleep(1)
        exit()
    else:
        break  
    
scores = []
while courses_number:
    try:
        score = float(input(f"please enter {len(scores) + 1}th grade,must be in (0,20):"))
        if not (0 <= score <= 20):
            raise OutOfRange(score,(0,20))
    except ValueError:
        print("grade must be float!!")
    except OutOfRange as e:
        print("Invalid Grade.", e)
        time.sleep(1)
        exit()
    else:
        scores.append(score)
        courses_number -= 1 
        
average = sum(scores) / len(scores)

print(grade(average))
