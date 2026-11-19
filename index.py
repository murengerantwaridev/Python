#----------------- Learning Python ----------------------------
#Remainding python3
#Creating variables
# this is a variable with a type of string
name = "murengerantwari"
#this is the variable with the type of integer
age=46
#this is a variable with the type of boolean
is_a_student = True
#a turple is an immutable list like structure variable
turple = (34,5,5,5,5,)
#a variable with the type of array that contains mutable values
list = [344,45,4556,56,56,]
#this is a disctonary containing key value pair
dictionary ={
    name:"Herve",
    age:34
}
#-----------  End og Basic Variables in Python --------------



#----------- Creating A calcualator in Python ---------------
# Remending of basic operation in ptyhon

num1=float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Enter an operation(/,-,+,*): ")
match operation:
    case "+":
        print(f"Addition {num1+num2}")
    case "-":
        print(f"Substraction {num1 - num2}")
    case "/":
        print(f"Division {num1+num2}")
    case "*":
        print(f"Multiplication {num1+num2}")
    case _:
        print("Operation unknown")
