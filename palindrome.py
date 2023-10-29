number=int(input("Enter Your Nmuber: "))
number1=number

reverse_number=0

while(number !=0):
    reverse_number=reverse_number*10+number%10
    number=int(number/10)

if reverse_number==number1:
    print(f"{reverse_number} is a palindrome number")
else:
    print(f"{reverse_number} is not a palindrome number")        

