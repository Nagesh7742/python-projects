#calculator app program

a = int(input('enter the a value: '))
b = int(input('enter the b value: '))
o = input("enter operation: ")
if o == "+":
    print(f'the anwer is = {a+b}')
elif o == "-":
    print(f'the anwer is = {a-b}')
elif o == "*":
    print(f'the anwer is = {a*b}')
else:
    print("invalid Operator")
    print("try again")

    
