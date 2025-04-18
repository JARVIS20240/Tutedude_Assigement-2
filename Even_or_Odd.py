#Taking User Input for Even or Odd Number:

number=int(input("Enter a number: "))

#Chack if the number is Even or Odd:

if (number%2==0) :
    print(number,"is an Even Number")
elif(number %2!=0):
    print(number,"is an Odd Number")
else:
    print("Please enter a valid number")
