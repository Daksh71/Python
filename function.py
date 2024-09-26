# # function can perform ant task
# # it can be reuse, function will return the result

# # create function to print the name
# def printName():
#     print("My name is Daksh Mittal")
    
# # call function to print the name
# printName()


# # create function to contenate fname and lname
# fname = input("Enter your first name : ")
# lname = input("Enter your last name : ")

# def printFullName(firstName,lastName):
#     print("Your full name is : ",firstName +" "+ lastName)
    
# printFullName(fname,lname)


# area of square using function
# def area(side):
#     print("Area of square is : ",side*side)
    
# area(8)

def area():
    side = int(input("Enter side of circle : "))
    area = side*side
    print("Area of circle is : ",area)
    
area()