print("bun venit la calculator")

bill = float(input("cat este nota? $"))

tip = int(input('Cat trebuie sa dam ciubuca? 10 12 15 '))

oameni = int(input("cati suntem?"))

bill_cu_tip = tip/100 * bill + bill

bill_per = bill_cu_tip / oameni

fill ="{:.2f}".format(round(bill_per,2))

print(f"fiecare trb sa dea : {fill}")

