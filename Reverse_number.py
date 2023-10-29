number=int(input("Enter your number:"))
print("Your number: ",number)

reverse_number=0

while(number !=0):
    reverse_number=reverse_number*10+(number%10)
    number=int(number/10)

print("Reverse Number",reverse_number)    