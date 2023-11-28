from secrets import choice


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b


def devide(a,b):
    return a/b

print("select operation : ")
print(" 1.add ")
print(" 2.subtract ")
print(" 3.multiply ")
print(" 4.divide ")

while True:
    choice = input("enter choice (1/2/3/4) : ")

    if choice in ('1' , '2' , ' 3' , '4'):
        try:
            num1 = float(input("enter frist number : "))
            num2 = float(input("enter second number : "))

        except ValueError:
            print("invalid input ! ")
            continue

        if choice == '1':
            print (num1 , "+" , num2 , "=" , add (num1,num2))

        elif choice == '2':
            print (num1 , "-" , num2 , "=" , sub (num1,num2))

        elif choice == '3':
            print (num1 , "*" , num2 , "=" , multi (num1,num2))

        elif choice == '4':
            print (num1 , "/" , num2 , "=" , devide (num1,num2))

        next_calculation = input("lets do next calculation ? (yes/no) : ")


        if next_calculation == "no":
            break

        elif next_calculation =="yes":
            continue

        else:
            print("invalid input")



