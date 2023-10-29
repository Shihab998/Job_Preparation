#Find leargest number using for loop

numbers=[63,67,98,32,45,34,987,456,21]

largest_number=0

for num in numbers:
    if largest_number < num:
       
       largest_number=num

print(largest_number)    

