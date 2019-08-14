number = int(input("Enter the number of items: "))
total=0
for i in range(number):

    price=float(input("The price of each item:"))
    total=total+price
    if total>100:
        payment=total*0.9
    else:payment=total
    print("Each price of items is",price)
print("The number of items are:",number,"The payment is:",payment)

