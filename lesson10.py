def check_age(age):
    if 10 <= age < 20:
        print("Student is allowed to enter the class.")
    else:
        print("Student is not allowed to enter the class.")

age = int(input("Enter the student's age: "))
check_age(age)
