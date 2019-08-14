print("Electricity bill estimator")
pricekWh=float(input("Enter cents per kWh: "))
Use=float(input("Enter consumption per kWh:"))
Number=float(input("Enter number of billing days:"))
estimatedBill=pricekWh*Use*Number/100
print(f"Estimated bill: ${estimatedBill:.2f}")

print("Electricity bill estimator 2.0")
TARIFF_11=0.244618
TARIFF_31=0.136928
tariff=int(input("Which tariff? 11 or 31: "))
while not(tariff==11 or tariff==31):
    tariff=int(input("Invalid. Enter 11 or 31"))
if tariff==11:
    tariffNumber=TARIFF_11
elif tariff==31:
    tariffNumber=TARIFF_31
    print("")
Use=float(input("Enter cents per kWh:"))
dayNumber=float(input("Enter number of billing days:"))
estimatedBill=dailyUse*dayNumber*Number
print(f'Estimated bill: ${estimatedBill:.2f}')