summa = input("give 1 number now, then keep giving more when prompted (10 in total): ")

for number in range (1,10):
    number = input("give next number: ")
    summa = summa + number

print "In total ", summa