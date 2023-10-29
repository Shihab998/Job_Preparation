#2100%4=0
#2100%100=0
#2100%400!=0 This year is not a leap year

#2000%4=0
#2000%100=0
#2000%400=0

#2012%4=0
#2012%100!=0
#2012%400!=0

year=int(input("Enter Your Year: "))

if(year%4==0 and (year%100!=0 or year%400==0)):
    print(f"{year} Year is a Leap Year")
else:
    print(f"{year} Year isn't a Leap Year")    