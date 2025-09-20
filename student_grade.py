def hasPassed(marks):
    if marks >= 35:
        return True
    else:
        return False
    
def studentsGrade(total_marks):
    average_marks = total_marks / 5 

    if total_marks >= 70:
        return "A"
    elif total_marks >= 60:
        return "B"
    else:
        return "C"
    

roll_no = int(input("Enter the roll no: "))
name = input("Enter the name: ")
maths_marks = float(input("Enter the marks in Maths : "))
english_marks = float(input("Enter the marks in English : "))
phy_science_marks = float(input("Enter the marks in Physics : "))
chemistry_marks = float(input("Enter the marks in Chemistry : "))
bio_science_marks = float(input("Enter the marks in Bio Science : "))

if(hasPassed(maths_marks) and hasPassed(english_marks) and hasPassed(phy_science_marks) and hasPassed(chemistry_marks) and hasPassed(bio_science_marks)):
    print("Student : {} has passed in all subjects".format(name))
    total_marks = maths_marks + english_marks + phy_science_marks + chemistry_marks + bio_science_marks
    grade = studentsGrade(total_marks)
    print("Total marks of student : {} is {} and grade is {}".format(name, total_marks, grade))  
        
else:
    print("Student :{} has failed in one or more subjects".format(name))
    if not hasPassed(maths_marks):
        print("Student :{} has failed in Maths".format(name))
    if not hasPassed(english_marks):
        print("Student :{} has failed in English".format(name))
    if not hasPassed(phy_science_marks):
        print("Student :{} has failed in Physics".format(name))
    if not hasPassed(chemistry_marks):
        print("Student :{} has failed in Chemistry".format(name))
    if not hasPassed(bio_science_marks):
        print("Student :{} has failed in Bio Science".format(name))
    print("{} has failed with Grade F".format(name))
